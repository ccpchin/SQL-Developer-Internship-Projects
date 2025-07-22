import sqlite3

conn = sqlite3.connect("airline.db")
cur = conn.cursor()

cur.execute("""
    SELECT airline, COUNT(*) as bookings
    FROM Bookings B
    JOIN Flights F ON B.flight_id = F.flight_id
    GROUP BY airline
""")
results = cur.fetchall()

print("📊 Booking Summary by Airline:")
for r in results:
    print(f"✈️ {r[0]} - {r[1]} bookings")

conn.close()