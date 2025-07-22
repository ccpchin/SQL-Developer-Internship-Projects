import sqlite3
import pandas as pd

df = pd.read_csv('flights.csv')

df['date_of_journey'] = pd.to_datetime(df['Date_of_Journey']).dt.date
df['dep_time'] = pd.to_datetime(df['Dep_Time'], format='%H:%M', errors='coerce').dt.time
df['seats_available'] = 180
df['dynamic_price'] = df['Price']

conn = sqlite3.connect('airline.db')
cur = conn.cursor()

for _, row in df.iterrows():
    row['date_of_journey'] = str(row['date_of_journey'])
    row['dep_time'] = row['dep_time'].strftime('%H:%M') if pd.notnull(row['dep_time']) else None
    cur.execute('''
        INSERT INTO Flights (
            airline, source, destination, date_of_journey, dep_time,
            duration, total_stops, additional_info, base_price,
            dynamic_price, seats_available
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        row['Airline'], row['Source'], row['Destination'],
        row['date_of_journey'], row['dep_time'],
        row['Duration'], row['Total_Stops'], row['Additional_Info'],
        row['Price'], row['dynamic_price'], row['seats_available']
    ))

conn.commit()
conn.close()