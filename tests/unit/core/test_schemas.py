import pytest

from app.core.schemas import BaseResponse, ErrorResponse


def test_success_response():
    """
    A successful response stores
    data correctly.
    """

    data = {
        "name": "Ram",
        "uid": 123,
    }

    response = BaseResponse(
        success=True,
        data=data,
    )

    assert response.success is True
    assert response.data == data
    assert response.error is None
    assert response.metadata is None


def test_error_response():
    """
    A failed response stores error
    information correctly.
    """

    error = ErrorResponse(
        code="UNAUTHORISED",
        message="You can't access",
        details=None,
    )

    response = BaseResponse(
        success=False,
        error=error,
    )

    assert response.success is False
    assert response.data is None
    assert response.error == {
        "code": "UNAUTHORISED",
        "message": "You can't access",
        "details": None,
    }


def test_success_response_cannot_have_error():
    """
    A successful response cannot include an error.
    """
    ...

    error = ErrorResponse(
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


def test_failed_response_cannot_have_data():
    """
    A failed response cannot include data.
    """

    with pytest.raises(
        ValueError,
        match="Failed response cannot contain data.",
    ):
        BaseResponse(
            success=False,
            data={"name": "Ram"},
        )


def test_to_dict():
    """
    Verifies that the response is serialized correctly to a dictionary.
    """

    response = BaseResponse(
        success=True,
        data={"name": "Ram"},
        metadata={"page": 1},
    )

    assert response.to_dict() == {
        "success": True,
        "data": {"name": "Ram"},
        "error": None,
        "metadata": {"page": 1},
    }


def test_error_response_details():
    """
    error details are preserved in the response.
    """

    error = ErrorResponse(
        code="VALIDATION_ERROR",
        message="Validation failed",
        details=[
            {"field": "email", "message": "Invalid email"}
        ],
    )

    response = BaseResponse(
        success=False,
        error=error,
    )

    assert response.error["details"] == [
        {"field": "email", "message": "Invalid email"}
    ]
