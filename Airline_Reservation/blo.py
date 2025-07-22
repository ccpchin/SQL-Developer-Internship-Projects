import sqlite3
from datetime import datetime

def make_booking(customer_id, flight_id, seat_number):
    conn = sqlite3.connect("airline.db")
    cur = conn.cursor()

    cur.execute("SELECT seats_available FROM Flights WHERE flight_id = ?", (flight_id,))
    row = cur.fetchone()

    if row and row[0] > 0:
        cur.execute('''
            INSERT INTO Bookings (customer_id, flight_id, seat_number, booking_date)
            VALUES (?, ?, ?, ?)
        ''', (customer_id, flight_id, seat_number, datetime.now().isoformat()))

        cur.execute('''
            UPDATE Flights SET seats_available = seats_available - 1
            WHERE flight_id = ?
        ''', (flight_id,))
        conn.commit()
        print("✅ Booking successful.")
    else:
        print("❌ No seats available.")

    conn.close()

def cancel_booking(booking_id):
    conn = sqlite3.connect("airline.db")
    cur = conn.cursor()

    cur.execute("SELECT flight_id FROM Bookings WHERE booking_id = ?", (booking_id,))
    row = cur.fetchone()

    if row:
        flight_id = row[0]

        cur.execute("DELETE FROM Bookings WHERE booking_id = ?", (booking_id,))
        cur.execute("UPDATE Flights SET seats_available = seats_available + 1 WHERE flight_id = ?", (flight_id,))
        conn.commit()
        print(f"✅ Booking {booking_id} cancelled.")
    else:
        print("❌ Booking ID not found.")

    conn.close()