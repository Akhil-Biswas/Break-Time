"""
app/auth/service.py

Business logic for authentication.
"""
from .schemas import (UserRegisterRequest,
    UserRegisterResponse
    )
from .models import Users
from .repository import UserRepository

def register_student(user: UserRegisterRequest) -> UserRegisterResponse:
    """
    Register a new student.

    Args:
        user: Validated registration data.

    Returns:
        UserRegisterResponse: Result of the registration process.
    """
    # business logic:
    # TODO: Check if email and phone already exist.
    # TODO: Hash the password before storing it.
        # Temporary: storing the password as plain text for development.
    user_password : str = user.password
    # 3. Map schema -> model.
    db_user : Users = Users(
        f_name=user.f_name,
        m_name=user.m_name,
        l_name=user.l_name,
        email=user.email,
        password_hash=user_password,
        phone=user.phone,
        photo=user.photo,
    )
    # 4. Save the user to the database.
    print(db_user.to_dict())
    try:
        repo : UserRepository = UserRepository()
        created_user : int = repo.create_user(db_user)

        # 5. Send a Confirmation

        print(f"Registering {user.email}")

        return UserRegisterResponse(
            message = "Student registered successfully.",
            success = True,
            user_id = created_user
        )
    except Exception as e:
        print(e)
        #raise
    finally:
        repo.close()