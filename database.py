import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='YOUR-PASSWORD-HERE', 
        database='job_tracker'
    )
