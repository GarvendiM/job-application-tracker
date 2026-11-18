import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password=' YOUR_MySQL_PASSWORD_HERE',
        database='job_tracker'
    )
