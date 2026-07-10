"""
app/core/exceptions.py

Global application exceptions.

This module defines a hierarchy of custom exceptions used throughout the
application. Each exception contains an HTTP status code and a default
message, making it suitable for API responses and centralized error handling.
"""

from typing import Any, Optional


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

    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    def __init__(
        self,
        message: Optional[str] = None,
        status_code: Optional[int] = None,
        code: Optional[str] = None,
        details: Any | None = None,
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
        Return a colored string representation of the exception.

        Returns:
            A formatted string containing the exception class name and message.
        """
        return (
            f"{self.RED}{self.BOLD}"
            f"{self.__class__.__name__}: {self.message}"
            f"{self.RESET}"
        )

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
    pass


class ServerException(AppException):
    pass

# ---------------------------------------------------------------------
# Client exceptions
# ---------------------------------------------------------------------


class BadRequestException(ClientException):
    """Exception raised for malformed or invalid client requests."""

    status_code = 400
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
    message = "Authentication is required or has failed."


class ForbiddenException(ClientException):
    """Exception raised when the authenticated user lacks permission."""

    status_code = 403
    message = "You do not have permission to perform this action."


class NotFoundException(ClientException):
    """Exception raised when a requested resource cannot be found."""

    status_code = 404
    message = "The requested resource was not found."


class ConflictException(ClientException):
    """Exception raised when a request conflicts with the current resource state."""

    status_code = 409
    message = "The request conflicts with the current state of the resource."


class UnprocessableEntityException(ClientException):
    """Exception raised when request validation fails."""

    status_code = 422
    message = "The request was well-formed but semantically invalid."


# ---------------------------------------------------------------------
# ServerException
# ---------------------------------------------------------------------


class InternalServerException(ServerException):
    """Exception raised for unexpected server-side failures."""

    status_code = 500
    message = "An internal server error occurred."


class DatabaseException(ServerException):
    """
    Base exception for all database-related errors.
    """

    status_code = 500
    message = "A database error occurred."


class DatabaseConnectionException(DatabaseException):
    status_code = 503
    message = "Failed to connect to the database."


class DatabaseQueryException(DatabaseException):
    message = "The database query could not be completed."


class DatabaseTransactionException(DatabaseException):
    message = "The database transaction failed."


class DatabaseIntegrityException(DatabaseException):
    status_code = 409
    message = "A database integrity constraint was violated."


class DatabaseTimeoutException(DatabaseException):
    status_code = 504
    message = "The database operation timed out."


if __name__ == "__main__":
    try:
        raise ValidationException("email","invalid email")
    except ValidationException as e:
        print(e)
        print(e.to_dict())
