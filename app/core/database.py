import mysql.connector
from app.core.config import Database

from mysql.connector import MySQLConnection

def db_connection() -> MySQLConnection:
    conn = mysql.connector.connect(
        host = Database.MYSQL_HOST,
        port = Database.MYSQL_PORT,
        user = Database.MYSQL_USER,
        password = Database.MYSQL_PASSWORD
    )
    return conn

if __name__ == "__main__":
    conn : MySQLConnection = db_connection()
    if conn.is_connected():
        print("MYSQL server is Connected Successfully....")
    else :
        print("Try Again ")

    conn.close()