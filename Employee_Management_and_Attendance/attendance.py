# attendance.py
from dbengine import get_connection
import random
from datetime import datetime, timedelta

def generate_attendance(emp_id, date):
    status = random.choice(["Present", "Late", "Absent"])
    check_in = "09:00" if status == "Present" else ("10:15" if status == "Late" else None)
    check_out = "17:00" if status in ["Present", "Late"] else None
    return (emp_id, date, check_in, check_out, status)

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT employee_id FROM Employees")
employee_ids = [row[0] for row in cur.fetchall()]

for emp_id in employee_ids:
    for i in range(5):
        day = (datetime.today() - timedelta(days=i)).strftime("%Y-%m-%d")
        emp_data = generate_attendance(emp_id, day)
        cur.execute('''
            INSERT INTO Attendance (employee_id, date, check_in, check_out, status)
            VALUES (%s, %s, %s, %s, %s)
        ''', emp_data)

conn.commit()
conn.close()
print("✅ Attendance simulated for 5 days.")