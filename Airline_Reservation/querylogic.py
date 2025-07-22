import sqlite3

def search_flights(source, destination, date):
    conn = sqlite3.connect("airline.db")
    cur = conn.cursor()

    cur.execute('''
        SELECT flight_id, airline, dep_time, seats_available, dynamic_price
        FROM Flights
        WHERE source = ? AND destination = ? AND date_of_journey = ? AND status = 'On-Time'
    ''', (source, destination, date))

    results = cur.fetchall()
    conn.close()

    if results:
        for r in results:
            print(f"Flight {r[0]} | Airline: {r[1]} | Dep: {r[2]} | Seats: {r[3]} | Price: ₹{r[4]}")
    else:
        print("No matching flights found.")