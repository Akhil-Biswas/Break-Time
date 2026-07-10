"""
app/core/exceptions.py

Global application exceptions.

This module defines a hierarchy of custom exceptions used throughout the
application. Each exception contains an HTTP status code and a default
message, making it suitable for API responses and centralized error handling.
"""

from typing import Any


class AppException(Exception):
    """
    Base exception for all application-specific errors.

    Attributes:
        status_code:
            HTTP status code associated with the exception.

        code:
            Machine-readable error code.

        message:
            Human-readable error message.

        details:
            Optional additional information describing the error.
    """

    status_code: int = 500
    code: str = "INTERNAL_SERVER_ERROR"
    message: str = "An unexpected error occurred."
    details: Any = None


    def __init__(
        self,
        message: str | None = None,
        status_code: int | None = None,
        code: str | None = None,
        details: Any = None,
    ) -> None:
        """
        Initialize an application exception.

        Args:
            message:
                Human-readable error message. If omitted, the class default
                ``message`` is used.

            status_code:
                HTTP status code. If omitted, the class default
                ``status_code`` is used.

            code:
                Machine-readable error code. If omitted, the class default
                ``code`` is used.

            details:
                Optional additional information about the error. This should
                contain only JSON-serializable data if it will be returned in
                an API response.
        """
        # Override the default values only when custom values are provided.
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code
        if code is not None:
            self.code = code

        self.details = details

        super().__init__(self.message)

    def __str__(self) -> str:
        """
        Return the exception message.

        Returns:
            The human-readable error message.
        """
        return self.message

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the exception into a serializable API error object.

        Returns:
            A dictionary containing the error code, message, and details.
        """
        return {
            "code": self.code,
            "message": self.message,
            "details": self.details,
        }


class ClientException(AppException):
    status_code = 400
    code = "CLIENT_ERROR"
    message = "A client error occurred."


class ServerException(AppException):
    status_code = 500
    code = "SERVER_ERROR"
    message = "A server error occurred."

# ---------------------------------------------------------------------
# Client exceptions
# ---------------------------------------------------------------------


class BadRequestException(ClientException):
    """Exception raised for malformed or invalid client requests."""

    status_code = 400
    code = "BAD_REQUEST"
    message = "The request was invalid."


class ValidationException(ClientException):
    """
    Raised when request validation fails.
    """
    status_code = 400
    code = "VALIDATION_ERROR"
    message = "Validation failed."

    def __init__(self, field: str, field_message: str):
        super().__init__(
            details={
                "field": field,
                "message": field_message,
            }
        )


class UnauthorizedException(ClientException):
    """Exception raised when authentication fails or is missing."""

    status_code = 401
    code = "UNAUTHORIZED"
    message = "Authentication is required or has failed."


class ForbiddenException(ClientException):
    """Exception raised when the authenticated user lacks permission."""

    status_code = 403
    code = "FORBIDDEN"
    message = "You do not have permission to perform this action."


class NotFoundException(ClientException):
    """Exception raised when a requested resource cannot be found."""

    status_code = 404
    code = "NOT_FOUND"
    message = "The requested resource was not found."


class ConflictException(ClientException):
    """Exception raised when a request conflicts with the current resource state."""

    status_code = 409
    code = "CONFLICT"
    message = "The request conflicts with the current state of the resource."


class UnprocessableEntityException(ClientException):
    """Exception raised when request validation fails."""

    status_code = 422
    code = "UNPROCESSABLE_ENTITY"
    message = "The request was well-formed but semantically invalid."


# ---------------------------------------------------------------------
# ServerException
# ---------------------------------------------------------------------


class InternalServerException(ServerException):
    """Exception raised for unexpected server-side failures."""

    status_code = 500
    code = "INTERNAL_SERVER_ERROR"
    message = "An internal server error occurred."


class DatabaseException(ServerException):
    """
    Base exception for all database-related errors.
    """

    status_code = 500
    code = "DATABASE_ERROR"
    message = "A database error occurred."


class DatabaseConnectionException(DatabaseException):
    status_code = 503
    code = "DATABASE_CONNECTION_ERROR"
    message = "Failed to connect to the database."


class DatabaseQueryException(DatabaseException):
    code = "DATABASE_QUERY_ERROR"
    message = "The database query could not be completed."


class DatabaseTransactionException(DatabaseException):
    code = "DATABASE_TRANSACTION_ERROR"
    message = "The database transaction failed."


class DatabaseIntegrityException(DatabaseException):
    status_code = 409
    code = "DATABASE_INTEGRITY_ERROR"
    message = "A database integrity constraint was violated."


class DatabaseTimeoutException(DatabaseException):
    status_code = 504
    code = "DATABASE_TIMEOUT"
    message = "The database operation timed out."


if __name__ == "__main__":
    try:
        raise ValidationException("email","invalid email")
    except ValidationException as e:
        print(e)
        print(e.to_dict())
    raise ValidationException("email","invalid email")
