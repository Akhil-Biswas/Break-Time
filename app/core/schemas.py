"""
app/core/schemas.py

Base Response Model

This module defines a generic response class that can be used to return
consistent API or application responses.
"""

from typing import Any, Optional


class ErrorResponse:
    def __init__(
        self,
        code: str,
        message: str,
        details: Optional[list | dict] = None,
    ) -> None:
        self.code = code
        self.message = message
        self.details = details

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
        error: Optional[ErrorResponse] = None,
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
            self.error: Any = None
        else:
            self.error: Any = error.__dict__

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
    import json

    # Example usage
    response = BaseResponse(True, {"name": "Ram"})
    #print(response.to_dict())


    class UserRegisterResponse(BaseResponse):
        def __init__(
            self,
            success: bool,
            data: Optional[Any] = None,
            error: Optional[Any] = None,
            metadata: Optional[Any] = None,
        ) -> None:

            super().__init__(
                success=success,
                data=data,
                error=error,
                metadata=metadata,
            )


    data = {
            "name" : "ram",
            "uid" : 123
        }

    error = ErrorResponse(
        code = "UNAUTHORISED",
        message = "you can't access",
        details = None
    )
    try:
        raise ValueError
        response = UserRegisterResponse(
            success = True,
            data = data
            )
    except ValueError as e:
        response = UserRegisterResponse(
            success = False,
            error = error
            )

    print(json.dumps(response.to_dict()))
