"""
app/auth/models.py
    
    Database data models
"""
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Users:
    """
    Represents a user account stored in the database.

    Attributes:
        id: Unique identifier of the user. Assigned by the database.
        f_name: User's first name.
        m_name: User's middle name, if available.
        l_name: User's last name.
        email: User's email address.
        password_hash: Hashed password used for authentication. (for now password is plain)
        phone: User's contact phone number.
        photo: Path or URL to the user's profile photo.
        address: User's residential or mailing address.
        role_id: Identifier of the user's assigned role.
        is_active: Indicates whether the account is active.
        created_at: Timestamp when the user record was created.
        updated_at: Timestamp when the user record was last updated.
        deleted_at: Soft-delete timestamp. ``None`` if the user is not deleted.
    """

    id: int | None = None
    f_name: str = ""
    m_name: str | None = None
    l_name: str = ""
    email: str = ""
    # for now we stored plain password
    password_hash: str = ""
    phone: str = ""
    photo: str | None = None
    address: str |None = None
    role_id: int = 3 # Student
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None

    def to_dict(self) -> dict[str, object]:
        """
        Return a dictionary representation of this user.

        This method uses ``dataclasses.asdict()`` to recursively convert
        the dataclass and any nested dataclasses (such as ``Name``)
        into standard Python dictionaries.

        Returns:
            dict[str, object]: Dictionary representation of the user.
        """
        return asdict(self)

if __name__ == "__main__":
    user = Users(
        f_name = "first",
        m_name = "middle",
        l_name = "last",
        password_hash = "password"
        )
    print(asdict(user))
    print(user.to_dict())