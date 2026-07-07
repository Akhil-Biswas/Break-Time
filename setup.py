from pathlib import Path

from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from app.core.config import Database
from app.core.database import mysql_connection



class DatabaseMigration:
    """Create the database and run SQL migrations."""

    def __init__(self, database_name: str) -> None:
        self.database_name = database_name

        self.conn: MySQLConnection = mysql_connection()
        self.cursor: MySQLCursor = self.conn.cursor()

    def create_database(self) -> None:
        """Create the database if it does not exist."""

        self.cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{self.database_name}`"
        )
        self.cursor.execute(
            f"USE `{self.database_name}`"
        )
        self.conn.commit()

    def run_migrations(self) -> None:
        self.create_database()

        migration_dir = Path("migrations")
        sql_files = sorted(migration_dir.glob("*.sql"))

        if not sql_files:
            print("No SQL migration files found.")
            return

        try:
            for sql_file in sql_files:
                print(f"Running {sql_file.name}...")

                sql = sql_file.read_text(encoding="utf-8")

                self.cursor.execute(sql)
                self.conn.commit()

                print(f"✓ {sql_file.name} completed")

            print("All migrations executed successfully.")

        except Error as err:
            self.conn.rollback()
            print(f"Migration failed: {err}")
            raise

        finally:
            self.cursor.close()
            self.conn.close()


if __name__ == "__main__":
    DatabaseMigration(Database.MYSQL_DATABASE).run_migrations()