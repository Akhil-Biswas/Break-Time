"""
app/core/exceptions.py

Global application exceptions.

This module defines a hierarchy of custom exceptions used throughout the
application. Each exception contains an HTTP status code and a default
message, making it suitable for API responses and centralized error handling.
"""

from typing import Optional


class AppException(Exception):
    """
    Base exception for all application-specific errors.

    Attributes:
        status_code: HTTP status code associated with the exception.
        message: Human-readable error message.
    """

    status_code: int = 500
    message: str = "An unexpected error occurred."

    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    def __init__(
        self,
        message: Optional[str] = None,
        status_code: Optional[int] = None,
    ) -> None:
        """
        Initialize the exception.

        Args:
            message:
                Custom error message. If omitted, the default class message
                is used.

            status_code:
                Custom HTTP status code. If omitted, the default class status
                code is used.
        """
        if message is not None:
            self.message = message

        if status_code is not None:
            self.status_code = status_code

        super().__init__(self.message)

    def __str__(self) -> str:
        """
        Return a colored string representation of the exception.

        Returns:
            A formatted string containing the exception class name and message.
        """
        return (
            f"      {self.RED}{self.BOLD}"
            f"{self.__class__.__name__}:{self.RESET} "
            f"{super().__str__()}"
        )

    def to_dict(self) -> dict[str, int | str]:
        """
        Convert the exception into a serializable dictionary.

        Returns:
            A dictionary containing the HTTP status code and message.
        """
        return {
            "status_code": self.status_code,
            "message": self.message,
        }


class BadRequestException(AppException):
    """Exception raised for malformed or invalid client requests."""

    status_code = 400
    message = "The request was invalid."


class UnauthorizedException(AppException):
    """Exception raised when authentication fails or is missing."""

    status_code = 401
    message = "Authentication is required or has failed."


class ForbiddenException(AppException):
    """Exception raised when the authenticated user lacks permission."""

    status_code = 403
    message = "You do not have permission to perform this action."


class NotFoundException(AppException):
    """Exception raised when a requested resource cannot be found."""

    status_code = 404
    message = "The requested resource was not found."


class ConflictException(AppException):
    """Exception raised when a request conflicts with the current resource state."""

    status_code = 409
    message = "The request conflicts with the current state of the resource."


class UnprocessableEntityException(AppException):
    """Exception raised when request validation fails."""

    status_code = 422
    message = "The request was well-formed but semantically invalid."


class InternalServerException(AppException):
    """Exception raised for unexpected server-side failures."""

    status_code = 500
    message = "An internal server error occurred."


if __name__ == "__main__":
    try:
        raise BadRequestException
    except AppException as e:
        print(e)
        print(e.to_dict())