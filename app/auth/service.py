"""
app/auth/service.py

Business logic for authentication.
"""
from .schemas import (UserRegisterRequest,
    UserRegisterResponse
    )
from .models import Users
from .repository import UserRepository
from app.core.database import db_connection
from app.core.exceptions import ( DatabaseConnectionException,
    DatabaseIntegrityException
)

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

    conn = None
    try:
        conn = db_connection()
        print("------------Conneced to database------------")
        repo : UserRepository = UserRepository(conn)

        created_user : int = repo.create_user(db_user)

        # 5. Send a Confirmation

        print(f"Registering {user.email}")

        return UserRegisterResponse(
            message = "Student registered successfully.",
            success = True,
            user_id = created_user
        )
    except DatabaseConnectionException as e:
        print("DatabaseException:", type(e), e)

    except DatabaseIntegrityException as e:
        print("DatabaseIntegrityException:", type(e), e)

    except Exception as e:
        print("Other:", type(e), e)

    finally:
        print("------------Service End------------")
        if conn is not None:
            conn.close()
