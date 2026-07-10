import pytest

from app.core.schemas import BaseResponse
from app.core.exceptions import (
    AppException,
    BadRequestException,
    UnauthorizedException,
    ForbiddenException,
    NotFoundException,
    ConflictException,
    ValidationException,
)


class TestBaseResponse:
    """
    Test suite for the BaseResponse class.

    Verifies:
    - Successful responses
    - Failed responses
    - Input validation
    - Dictionary serialization
    """
    # Success
    # Failure
    # Validation
    # Serialization
    # Edge Cases
    @pytest.mark.parametrize(
        ("data", "metadata"),
        [
            (
                {"name": "Ram"},
                {"page": 1},
            ),
            (
                {"name": "Ram", "uid": 123},
                None,
            ),
        ],
    )
    def test_stores_data_for_successful_response(self, data, metadata):
        """
        A successful response stores data correctly.
        """
        response = BaseResponse(
            success=True,
            data=data,
            metadata=metadata,
        )

        assert response.success is True
        assert response.data == data
        assert response.error is None
        assert response.metadata == metadata

    @pytest.mark.parametrize(
        "error",
        [
            BadRequestException(),
            UnauthorizedException(),
            ForbiddenException(),
            NotFoundException(),
            ConflictException(),
            ValidationException(
                field="email",
                field_message="Invalid email",
            ),
            AppException(
                code="CUSTOM_ERROR",
                message="Something went wrong",
            ),
        ],
    )
    def test_stores_error_for_failed_response(self, error):
        """
        A failed response stores error information correctly.
        """
        response = BaseResponse(
            success=False,
            error=error,
        )

        assert response.success is False
        assert response.data is None
        assert response.error == error.to_dict()
        assert response.metadata is None

    def test_success_rejects_error(self):
        error = AppException(
            code="ERR001",
            message="Some error",
        )

        with pytest.raises(
            ValueError,
            match="Successful response cannot contain an error.",
        ):
            BaseResponse(
                success=True,
                data={"name": "Ram"},
                error=error,
            )

    def test_failure_rejects_data(self):
        with pytest.raises(
            ValueError,
            match="Failed response cannot contain data.",
        ):
            BaseResponse(
                success=False,
                data={"name": "Ram"},
            )

    @pytest.mark.parametrize(
        ("data", "metadata"),
        [
            (
                {"name": "Ram"},
                {"page": 1},
            ),
            (
                {"name": "Ram", "uid": 123},
                None,
            ),
        ],
    )
    def test_to_dict_success(self, data, metadata):
        response = BaseResponse(
            success=True,
            data=data,
            metadata=metadata,
        )

        assert response.to_dict() == {
            "success": True,
            "data": data,
            "error": None,
            "metadata": metadata,
        }

    def test_to_dict_failure(self):
        error = ValidationException(
            field="email",
            field_message="Invalid email",
        )

        response = BaseResponse(
            success=False,
            error=error,
        )

        assert response.to_dict() == {
            "success": False,
            "data": None,
            "error": error.to_dict(),
            "metadata": None,
        }

    def test_error_details(self):
        error = AppException(
            code="VALIDATION_ERROR",
            message="Validation failed",
            details=[
                {
                    "field": "email",
                    "message": "Invalid email",
                }
            ],
        )

        response = BaseResponse(
            success=False,
            error=error,
        )

        assert response.error["code"] == "VALIDATION_ERROR"
        assert response.error["message"] == "Validation failed"
        assert response.error["details"] == [
            {
                "field": "email",
                "message": "Invalid email",
            }
        ]

    @pytest.mark.parametrize(
        "value",
        [
            "yes",
            1,
            0,
            None,
            [],
            {},
        ],
    )
    def test_success_must_be_boolean(self, value):
        with pytest.raises(
            TypeError,
            match="success must be a boolean.",
        ):
            BaseResponse(
                success=value,
                data={"name": "Ram"},
            )

    @pytest.mark.parametrize(
        "value",
        [
            "error",
            123,
            [],
            {},
            object(),
        ],
    )
    def test_error_must_be_app_exception(self,value):
        with pytest.raises(
            TypeError,
            match="error must be an AppException.",
        ):
            BaseResponse(
                success=False,
                error=value,
            )
