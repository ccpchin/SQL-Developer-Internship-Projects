import psycopg2
from dbengine import get_connection

def find_by_department(dept):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT employee_id, name, job_role FROM Employees WHERE department = %s", (dept,))
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Role: {row[2]}")