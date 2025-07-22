import sqlite3

schema = """
CREATE TABLE IF NOT EXISTS Flights (
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    airline TEXT,
    source TEXT,
    destination TEXT,
    date_of_journey TEXT,
    dep_time TEXT,
    duration TEXT,
    total_stops TEXT,
    additional_info TEXT,
    base_price REAL,
    dynamic_price REAL,
    total_seats INTEGER DEFAULT 180,
    seats_available INTEGER,
    status TEXT DEFAULT 'On-Time'
);

CREATE TABLE IF NOT EXISTS Bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    flight_id INTEGER,
    seat_number TEXT,
    booking_date TEXT
);

CREATE TABLE IF NOT EXISTS Booking_Audit (
    audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    action_type TEXT,
    booking_id INTEGER,
    changed_on TEXT DEFAULT (datetime('now')),
    performed_by TEXT
);
"""

conn = sqlite3.connect("airline.db")
cursor = conn.cursor()
cursor.executescript(schema)
conn.commit()
conn.close()
print("✅ Database schema created and initialized successfully.")