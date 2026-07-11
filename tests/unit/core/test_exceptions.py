import pytest
from app.core.exceptions import (
    AppException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ConflictException,
    UnprocessableEntityException,
    InternalServerException,
    DatabaseConnectionException,
    DatabaseQueryException,
    DatabaseTransactionException,
    DatabaseIntegrityException,
    DatabaseTimeoutException,
    ValidationException,
)


class TestAppException:
    def test_uses_default_values(self):
        exc = AppException()

        assert exc.status_code == 500
        assert exc.message == "An unexpected error occurred."

    def test_accepts_custom_values(self):
        exc = AppException(
            message="Custom error",
            status_code=404,
        )

        assert exc.status_code == 404
        assert exc.message == "Custom error"

    def test_to_dict(self):
        exc = AppException(
            message="Error",
            status_code=400,
        )

        assert exc.to_dict() == {
            "code": "INTERNAL_SERVER_ERROR",
            "message": "Error",
            "details": None,
        }

    def test_string_representation(self):
        exc = AppException(
            message="Something went wrong",
            status_code=500,
        )

        text = str(exc)

        assert text == "Something went wrong"


class TestHttpExceptions:
    @pytest.mark.parametrize(
        ("exception", "status_code", "message"),
        [
            (BadRequestException, 400, "The request was invalid."),
            (
                UnauthorizedException,
                401,
                "Authentication is required or has failed.",
            ),
            (
                ForbiddenException,
                403,
                "You do not have permission to perform this action.",
            ),
            (
                NotFoundException,
                404,
                "The requested resource was not found.",
            ),
            (
                ConflictException,
                409,
                "The request conflicts with the current state of the resource.",
            ),
            (
                UnprocessableEntityException,
                422,
                "The request was well-formed but semantically invalid.",
            ),
            (
                InternalServerException,
                500,
                "An internal server error occurred.",
            ),
        ],
    )
    def test_defaults(self, exception, status_code, message):
        exc = exception()

        assert exc.status_code == status_code
        assert exc.message == message


class TestDatabaseExceptions:
    @pytest.mark.parametrize(
        ("exception", "status_code", "message"),
        [
            (
                DatabaseConnectionException,
                503,
                "Failed to connect to the database.",
            ),
            (
                DatabaseQueryException,
                500,
                "The database query could not be completed.",
            ),
            (
                DatabaseTransactionException,
                500,
                "The database transaction failed.",
            ),
            (
                DatabaseIntegrityException,
                409,
                "A database integrity constraint was violated.",
            ),
            (
                DatabaseTimeoutException,
                504,
                "The database operation timed out.",
            ),
        ],
    )
    def test_defaults(self, exception, status_code, message):
        exc = exception()

        assert exc.status_code == status_code
        assert exc.message == message


class TestValidationException:
    @pytest.mark.parametrize(
        ("field", "detail"),
        [
            ("email", "Email must contain @."),
            ("username", "Username is required."),
            ("password", "Password must be at least 8 characters."),
        ],
    )
    def test_validation_error(self, field, detail):
        exc = ValidationException(field, detail)

        assert exc.status_code == 400
        assert exc.code == "VALIDATION_ERROR"
        assert str(exc) == "Validation failed."

        assert exc.to_dict() == {
            "code": "VALIDATION_ERROR",
            "message": "Validation failed.",
            "details": {
                "field": field,
                "message": detail,
            },
        }