"""
app/auth/repository.py

Database access layer
    • Execute SQL queries.
    • Pass query parameters.
    • Map database rows to models.
    • Return dataclass objects
"""
from datetime import datetime
from typing import Optional

from mysql.connector import errors
from app.core.database import translate_mysql_exception


from .queries import (
    CREATE_USER,
    GET_ALL_USER,
    GET_USER_BY_ID,
    GET_USER_BY_EMAIL,
    SOFT_DELETE_USER,
    RESTORE_USER,
)
from .models import Users


class UserRepository:
    """Provides CRUD operations for the users table."""
    def __init__(self, conn):
        """Initialize a database connection."""
        self.conn = conn

    def _new_cursor(self):
        """Return a new database cursor."""
        return self.conn.cursor()

    def create_user(self, user: Users) -> int:
        """
        Insert a new user into the database.

        Args:
            user: User object containing user information.

        Returns:
            The ID of the newly created user.
        """
        try:
            cursor = self._new_cursor()
            cursor.execute(
                    CREATE_USER,
                (
                    user.f_name,
                    user.m_name,
                    user.l_name,
                    user.email,
                    user.password_hash,
                    user.phone,
                    user.photo,
                    user.address,
                    user.role_id,
                    user.is_active,
                    #datetime.now(), by database
                    #datetime.now(), by database
                ),
            )
            self.conn.commit()
            return cursor.lastrowid
        except errors.Error as e:
            translate_mysql_exception(e)
        finally:
            if cursor is not None:
                cursor.close()

    def get_by_id(self, user_id: int) -> Optional[Users]:
        """
        Retrieve a user by its ID.

        Args:
            user_id: Primary key of the user.

        Returns:
            A Users object if found, otherwise None.
        """
        try:
            cursor = self._new_cursor()
            cursor.execute(GET_USER_BY_ID, (user_id,))
            row = cursor.fetchone()

            if row is None:
                return None

            return Users(**dict(row))
        except errors.Error as e:
            translate_mysql_exception(e)
        finally:
            if cursor is not None:
                cursor.close()

    def get_by_email(self, email: str) -> Optional[Users]:
        """
        Retrieve a user by email address.

        Args:
            email: User email address.

        Returns:
            A Users object if found, otherwise None.
        """
        try:
            cursor = self._new_cursor()
            cursor.execute(GET_USER_BY_EMAIL, (email,))
            row = cursor.fetchone()

            if row is None:
                return None

            return Users(**dict(row))
        except errors.Error as e:
            translate_mysql_exception(e)
        finally:
            if cursor is not None:
                cursor.close()

    def get_all_users(self) -> list[Users]:
        """
        Retrieve all active users.

        Returns:
            A list of Users objects.
        """
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(GET_ALL_USER)

            return [Users(**dict(row)) for row in cursor.fetchall()]
        except errors.Error as e:
            translate_mysql_exception(e)
        finally:
            if cursor is not None:
                cursor.close()

    # UPDATE USER


    def soft_delete_user(self, user_id: int) -> bool:
        """
        Soft-delete a user.

        The record is not removed from the database.
        Instead, the deleted_at column is updated.

        Args:
            user_id: ID of the user.

        Returns:
            True if a record was updated, otherwise False.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                SOFT_DELETE_USER,
                (datetime.now(), user_id),
            )

            self.conn.commit()
            return cursor.rowcount > 0
        except errors.Error as e:
            translate_mysql_exception(e)
        finally:
            if cursor is not None:
                cursor.close()

    def restore_user(self, user_id: int) -> bool:
        """
        Restore a soft-deleted user.

        Args:
            user_id: ID of the user.

        Returns:
            True if the user was restored, otherwise False.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                RESTORE_USER,
                (user_id,),
            )

            self.conn.commit()
            return cursor.rowcount > 0
        except errors.Error as e:
            translate_mysql_exception(e)
        finally:
            if cursor is not None:
                cursor.close()

if __name__ == "__main__":
    pass
