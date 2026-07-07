"""
app/auth/routes.py

HTTP request/response handling.
    • Define Flask routes.
    • Receive HTTP requests.
    • Call schemas and services.
    • Render templates.
    • Return JSON responses or redirects.
"""
from flask import Blueprint, request
from flask.typing import ResponseReturnValue
from .schemas import UserRegisterRequest,UserRegisterResponse
from .service import register_student

# Create a Blueprint named "auth" to organize authentication-related routes.
auth = Blueprint("auth", __name__)

@auth.route("/auth/student/register",
    methods=["GET", "POST"]
    )
def student_register() -> ResponseReturnValue:
    """
    Display the registration page or process a registration request.

    Returns:
        ResponseReturnValue: A Flask response.
    """

    if request.method == "POST":
        try:
            form_data: dict[str, str] = request.form.to_dict()

            user: UserRegisterRequest = UserRegisterRequest(**form_data)

            result : UserRegisterResponse = register_student(user)
            if result is None:
                return {"error": "Registration failed"}, 400

            return result.to_dict(), 200

        except ValueError as e:
            return {"error": str(e)}, 400

    return "Signup Page"


@auth.route("/auth/login",
    methods=["GET","POST"]
    )
def login() -> ResponseReturnValue:
    """
    Display the login page or process a login request.

    Returns:
        ResponseReturnValue: A Flask response.
    """
    return "Login Page"

@auth.route("/auth/logout",
    methods=["POST"]
    )
def logout() -> ResponseReturnValue:
    """
    Log out the current user.

    Returns:
        ResponseReturnValue: A Flask response.
    """
    return "Logout Successful"

if __name__ == '__main__':
    pass