from typing import NoReturn

import mysql.connector
from app.core.config import Database
from mysql.connector import errors

from app.core.exceptions import (
    InternalServerException,
    DatabaseException,
    DatabaseConnectionException,
    DatabaseQueryException,
    DatabaseTransactionException,
    DatabaseIntegrityException,
    DatabaseTimeoutException,
)

def mysql_connection():
    """
    Connect to the MySQL server without selecting a database.
    """
    try:
        conn = mysql.connector.connect(
            host=Database.MYSQL_HOST,
            port=Database.MYSQL_PORT,
            user=Database.MYSQL_USER,
            password=Database.MYSQL_PASSWORD,
        )
        return conn
    except errors.Error as e:
        translate_mysql_exception(e)
    except Exception as e:
        raise InternalServerException(str(e)) from e


def db_connection():
    """
    Connect to the MySQL server and select the configured database.
    """
    try:
        conn = mysql.connector.connect(
            host=Database.MYSQL_HOST,
            port=Database.MYSQL_PORT,
            user=Database.MYSQL_USER,
            password=Database.MYSQL_PASSWORD,
            database=Database.MYSQL_DATABASE,
        )
        return conn
    except errors.Error as e:
        translate_mysql_exception(e)
    except Exception as e:
        raise InternalServerException(str(e)) from e

def translate_mysql_exception(exc: errors.Error) -> NoReturn:
    """
    Convert MySQL Connector exceptions into application exceptions.
    """

    if not isinstance(exc, errors.Error):
        raise TypeError(f"Expected mysql.connector.errors.Error, got {type(exc).__name__}")

   # --- InterfaceError: connection could not be established / communication failure
    # errno 2003 = Can't connect to MySQL server
    # errno 2002 = Can't connect through socket
    if isinstance(exc, errors.InterfaceError):
        raise DatabaseConnectionException(str(exc)) from exc

    # --- PoolError: connection pool exhausted or unavailable
    # (no single errno — raised by the connector's pool manager itself, not MySQL server)
    if isinstance(exc, errors.PoolError):
        raise DatabaseConnectionException(str(exc)) from exc

    # --- OperationalError: needs errno-level sub-dispatch (4 sub-cases)
    if isinstance(exc, errors.OperationalError):

        # (1) Connection failure
        # errno 2006 = MySQL server has gone away
        # errno 2013 = Lost connection to MySQL server during query
        # errno 2003 = Can't connect to MySQL server (can also surface here)
        if exc.errno in (2006, 2013, 2003):
            raise DatabaseConnectionException(str(exc)) from exc

        # (2) Timeout
        # errno 1205 = Lock wait timeout exceeded
        if exc.errno in (1205,):
            raise DatabaseTimeoutException(str(exc)) from exc

        # (3) Transaction failure (deadlock)
        # errno 1213 = Deadlock found when trying to get lock
        if exc.errno in (1213,):
            raise DatabaseTransactionException(str(exc)) from exc

        # (4) Other operational errors not covered above
        # errno 1040 = Too many connections
        # errno 1053 = Server shutdown in progress
        raise DatabaseQueryException(str(exc)) from exc

    # --- IntegrityError: constraint violations
    # errno 1062 = Duplicate entry for key (unique constraint)
    # errno 1451 = Cannot delete/update parent row (FK constraint)
    # errno 1452 = Cannot add/update child row (FK constraint)
    # errno 1048 = Column cannot be null
    if isinstance(exc, errors.IntegrityError):
        raise DatabaseIntegrityException(str(exc)) from exc

    # --- DataError, InternalError, ProgrammingError, NotSupportedError, generic DatabaseError
    # errno 1406 = Data too long for column        (DataError)
    # errno 1264 = Out of range value for column    (DataError)
    # errno 1364 = Field doesn't have default value (InternalError, in some driver versions)
    # errno 1146 = Table doesn't exist               (ProgrammingError)
    # errno 1054 = Unknown column                    (ProgrammingError)
    # errno 1064 = SQL syntax error                  (ProgrammingError)
    if isinstance(exc, (errors.DataError,
                        errors.InternalError,
                        errors.ProgrammingError,
                        errors.NotSupportedError,
                        errors.DatabaseError)):
        raise DatabaseQueryException(str(exc)) from exc

    # Base class for all mysql.connector exceptions
    raise DatabaseException(str(exc)) from exc

if __name__ == "__main__":
    try:
        conn = mysql_connection()
        if conn.is_connected():
            print("Connected to MySQL Server.")
        conn.close()

        db_conn = db_connection()
        if db_conn.is_connected():
            print(f"Connected to database: {Database.MYSQL_DATABASE}")
        db_conn.close()
    except DatabaseException as e:
        print(f"Database error: {e.message}")