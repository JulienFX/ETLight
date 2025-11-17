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
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("Table was created.")
    except psycopg2.Error as e:
        print(f"Failed to create table : {e}")
        raise

def inserted_records(conn,data) :
    print("Inserting weather data into the db ...")
    try: 
        weather = data['current']
        location = data['location']
        cursor=conn.cursor()
        # req sql à faire suivi des valeurs brutes à insérer
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                inserted_at,
                utc_offset
            ) VALUES(%s, %s, %s, %s, %s, NOW(), %s)
        """,(
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        )
        )
        conn.commit()
        print("Data succesfully inserted")
    except psycopg2.Error as e:
        print(f"Error inserting data into the database: {e}")
        raise
# simulation appel d'API, on simule pour ne pas utiliser pour rien le nombre de requête limité à 100
data = mock_fetch_data()
# connection à la bdd
conn = connect_to_db()
# creation table + remplissage avec enregistrements
create_table(conn)
inserted_records(conn,data)
