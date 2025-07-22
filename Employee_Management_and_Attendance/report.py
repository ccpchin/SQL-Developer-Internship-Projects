import psycopg2
from dbengine import get_connection

def generate_attendance_report():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT employee_id,
               ROUND(SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END)*100.0 / COUNT(*), 1) AS attendance_ratio
        FROM Attendance
        GROUP BY employee_id
        HAVING COUNT(*) >= 3
        ORDER BY attendance_ratio DESC;
    """)
    results = cur.fetchall()

    print("📊 Attendance Ratios:")
    for row in results:
        print(f"Employee {row[0]}: {row[1]}%")

    conn.close()