import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Connexion à la base PostgreSQL réussie")
        return conn
    except psycopg2.Error as e:
        print("Erreur de connexion à PostgreSQL :", e)
        return None
    
