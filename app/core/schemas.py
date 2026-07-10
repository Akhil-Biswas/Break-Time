"""
app/core/schemas.py

Base Response Model

This module defines a generic response class that can be used to return
consistent API or application responses.
"""

from typing import Any, Optional
from app.core.exceptions import AppException


class BaseResponse:
    """
    A generic response object.

    Attributes:
        success (bool): Indicates whether the operation was successful.
        data (Any): The response data.
        error (Any): Error details if the operation failed.
        metadata (Any): Additional information about the response.
    """

    def __init__(
        self,
        success: bool,
        #message: str,
        data: Optional[dict[str, Any]] = None,
        error: Optional[AppException] = None,
        metadata: Optional[Any] = None,
    ) -> None:
        """
        Initialize the response object.

        Args:
            success (bool): True if the operation succeeded.
            data (Any, optional): Response payload.
            error (Any, optional): Error information.
            metadata (Any, optional): Extra response metadata.
        """

        if success and error is not None:
            raise ValueError("Successful response cannot contain an error.")

        if not success and data is not None:
            raise ValueError("Failed response cannot contain data.")

        # Status of the operation
        self.success: bool = success

        #self.message = message

        # Response payload
        self.data: Any = data

        # Error information
        if error is None:
            self.error = None
        else:
            self.error = error.to_dict()

        # Additional metadata
        self.metadata: Any = metadata

    def to_dict(self) -> dict[str,Any]:
        """
        Convert the response object into a dictionary.

        Returns:
            dict[str, Any]: Dictionary representation of the response.
        """
        return {
            "success": self.success,
            "data": self.data,
            "error": self.error,
            "metadata": self.metadata,
        }


if __name__ == "__main__":
    pass
