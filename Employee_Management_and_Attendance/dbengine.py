# db_engine.py
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="employee",
        user="postgres",
        password="Daddy$444",  
        host="localhost",
        port="5432"
    )