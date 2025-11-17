import psycopg2
from api_request import mock_fetch_data

def connect_to_db() :
    print("Connecting to the PostgreSQL database...")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5000,
            dbname="db",
            user="admin",
            password="admin"
        )
        return conn
    except psycopg2.Error as e: 
        print(f"Databse connection failed: {e}")
        raise 

def create_table(conn) :
    print("Creating table if not exist...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev
        """)