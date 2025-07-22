import sqlite3
from datetime import datetime

def log_audit(action_type, booking_id, performed_by="system_user"):
    conn = sqlite3.connect("airline.db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Booking_Audit (action_type, booking_id, changed_on, performed_by)
        VALUES (?, ?, ?, ?)
    ''', (action_type, booking_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), performed_by))
    conn.commit()
    conn.close()