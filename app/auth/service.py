"""
app/auth/service.py

Business logic for authentication.
"""
from .schemas import UserRegisterRequest

def register_student(user: UserRegisterRequest) -> dict[str, str]:
    """
    Register a new student.

    Args:
        user: Validated registration data.

    Returns:
        dict[str, str]: Result of the registration process.
    """
    # business logic:
    # 1. Check if the email and phone already exists.
    # 2. Hash the password.
    # 3. Save the user to the database.
    # 4. Send a verification email.

    print(f"Registering {user.email}")

    return {
        "message": "Student registered successfully."
    }