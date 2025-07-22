# workhours.py
from dbengine import get_connection


def calculate_total_work_hours():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT employee_id,
               COUNT(*) FILTER (WHERE check_in IS NOT NULL AND check_out IS NOT NULL) AS days_present,
               SUM(EXTRACT(EPOCH FROM (check_out::time - check_in::time)) / 3600) AS total_hours
        FROM Attendance
        WHERE status IN ('Present', 'Late')
        GROUP BY employee_id
        HAVING COUNT(*) > 0
    """)

    results = cur.fetchall()
    conn.close()

    print("\n⏱️ Total Work Hours Report:")
    for emp_id, days_present, total_hours in results:
        print(f"Employee {emp_id}: {total_hours:.2f} hours across {days_present} days")


if __name__ == "__main__":
    calculate_total_work_hours()