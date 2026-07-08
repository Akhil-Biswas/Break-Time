import mysql.connector
from app.core.config import Database

def mysql_connection():
    """
    Connect to the MySQL server without selecting a database.
    """
    conn = mysql.connector.connect(
        host=Database.MYSQL_HOST,
        port=Database.MYSQL_PORT,
        user=Database.MYSQL_USER,
        password=Database.MYSQL_PASSWORD,
    )
    return conn


def db_connection():
    """
    Connect to the MySQL server and select the configured database.
    """
    conn = mysql.connector.connect(
        host=Database.MYSQL_HOST,
        port=Database.MYSQL_PORT,
        user=Database.MYSQL_USER,
        password=Database.MYSQL_PASSWORD,
        database=Database.MYSQL_DATABASE,
    )
    return conn


if __name__ == "__main__":
    # Without database
    conn = mysql_connection()
    if conn.is_connected():
        print("Connected to MySQL Server.")
    conn.close()

    # With database
    db_conn = db_connection()
    if db_conn.is_connected():
        print(f"Connected to database: {Database.MYSQL_DATABASE}")
    db_conn.close()