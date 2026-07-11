"""
Unit tests for the MySQL exception handler.
"""
import pytest
from mysql.connector import errors

from app.core.database import translate_mysql_exception
from app.core.exceptions import (
    InternalServerException,
    DatabaseException,
    DatabaseConnectionException,
    DatabaseQueryException,
    DatabaseTransactionException,
    DatabaseIntegrityException,
    DatabaseTimeoutException,
)


# Verify that each MySQL connector exception is translated
# into the corresponding application-specific exception.
@pytest.mark.parametrize(
    "mysql_exc, expected_exc",
    [
        # InterfaceError -> connection
        (errors.InterfaceError(), DatabaseConnectionException),

        # PoolError -> connection
        (errors.PoolError(), DatabaseConnectionException),

        # OperationalError sub-cases (errno-dependent)
        (errors.OperationalError(errno = 2003), DatabaseConnectionException),  # can't connect
        (errors.OperationalError(errno = 2006), DatabaseConnectionException),  # server gone away
        (errors.OperationalError(errno = 2013), DatabaseConnectionException),  # lost during query
        (errors.OperationalError(errno = 1205), DatabaseTimeoutException),     # lock wait timeout
        (errors.OperationalError(errno = 1213), DatabaseTransactionException), # deadlock
        (errors.OperationalError(errno = 9999), DatabaseQueryException),       # unmapped errno -> "Other"

        # IntegrityError -> integrity
        (errors.IntegrityError(), DatabaseIntegrityException),

        # DataError, InternalError, ProgrammingError, NotSupportedError, DatabaseError -> query
        (errors.DataError(), DatabaseQueryException),
        (errors.InternalError(), DatabaseQueryException),
        (errors.ProgrammingError(), DatabaseQueryException),
        (errors.NotSupportedError(), DatabaseQueryException),
        (errors.DatabaseError(), DatabaseQueryException),

        # Base Error
        (errors.Error(), DatabaseException),
    ]
)
def test_translate_mysql_exception(mysql_exc, expected_exc):
    print(isinstance(mysql_exc, errors.Error))
    with pytest.raises(expected_exc):
        translate_mysql_exception(mysql_exc)


# Verify that unsupported exception types are rejected
# instead of being treated as MySQL connector exceptions.
@pytest.mark.parametrize(
    "mysql_exc",
    [
        "",
        "abc",
        [],
        [1,2],
        {},
        Exception("XYZ"),
        errors.Warning(),
        ValueError("XYZ"),
        DatabaseException(),
    ],
)
def test_error_if_not_mysql_error(mysql_exc):
    with pytest.raises(TypeError):
        translate_mysql_exception(mysql_exc)
