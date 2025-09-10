import time
import os
import psycopg2
from psycopg2 import OperationalError

def db_wait():    
    max_retries = 10
    retry_delay = 3
    
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(
                dbname=os.environ.get('POSTGRES_DB', 'qna_db'),
                user=os.environ.get('POSTGRES_USER', 'postgres'),
                password=os.environ.get('POSTGRES_PASSWORD', 'password'),
                host=os.environ.get('POSTGRES_HOST', 'db'),
                port=os.environ.get('POSTGRES_PORT', '5432')
            )
            conn.close()
            print("Database is ready!")
            return True
        except OperationalError:
            print(f"Waiting for database... (attempt {i+1}/{max_retries})")
            time.sleep(retry_delay)
    
    print("Database connection failed after multiple attempts")
    return False

if __name__ == "__main__":
    db_wait()