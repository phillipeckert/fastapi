from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# Standard Copy & Paste stuff to establishing connection to DB and to create session
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine) 

Base = declarative_base()

def get_db(): # Get a session from the database.py file via SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
# Not in use, with this we can run raw SQL, but with sqlalchemy we dont need it:
while True: # Connector to database
    try: 
        conn = psycopg2.connect(host = 'localhost', database='fastapi', 
                                user='postgres', password='0511', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error was", error)
        time.sleep(2)
"""