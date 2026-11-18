import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='databaseclasscool7!',
        database='job_tracker'
    )