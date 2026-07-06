"""
app/auth/schemas.py

Request and response schemas.
    • Define request models.
    • Define response models.
    • Validate user input.
"""


class UserRegisterRequest:
    """
    Request model for user registration.

    This class represents the data submitted by a client when
    creating a new user account.

    Attributes:
        f_name: User's first name.
        m_name: User's middle name (optional).
        l_name: User's last name.
        email: User's email address.
        password: Plain-text password provided by the user.
        phone: User's phone number.
        photo: Profile photo URL or file path (optional).
        address: User's address (optional).
    """

    def __init__(
        self,
        f_name: str,
        m_name: str | None = None,
        l_name: str = "",
        email: str = "",
        password: str = "",
        phone: str = "",
        photo: str | None = None,
        #address: str | None = None,
    ) -> None:
        """
        Initialize a new user registration request.

        Args:
            f_name: User's first name.
            m_name: User's middle name.
            l_name: User's last name.
            email: User's email address.
            password: Plain-text password.
            phone: User's phone number.
            photo: Profile photo URL or path.
            address: User's address.
        """
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.email = self._validate_email(email)
        self.phone = self._validate_phone(phone)
        self.photo = photo
        #self.address = address
        self.password = self._validate_password(password)

    @staticmethod
    def _validate_email(email: str) -> str:
        """
        Validate the email address.

        Args:
            email: Email address to validate.

        Returns:
            The validated email address.

        Raises:
            ValueError: If the email is missing or invalid.
        """
        if not email:
            raise ValueError("Email is required.")
        if "@" not in email:
            raise ValueError("Invalid email address.")
        return email

    @staticmethod
    def _validate_phone(phone: str | int) -> str:
        """
        Validate an Indian phone number.

        Accepts a string or integer. Spaces and hyphens are removed
        before validation.

        Examples:
            9876543210
            "9876543210"
            "987 654 3210"
            "987-654-3210"

        Args:
            phone: Phone number to validate.

        Returns:
            The normalized 10-digit phone number.

        Raises:
            ValueError: If the phone number is missing or invalid.
        """
        if phone is None:
            raise ValueError("Phone number is required.")

        phone = str(phone).strip()
        phone = phone.replace("-", "").replace(" ", "")

        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits.")

        if len(phone) != 10:
            raise ValueError("Phone number must be 10 digits.")

        return phone

    @staticmethod
    def _validate_password(password: str) -> str:
        """
        Validate the password.

        Args:
            password: Password to validate.

        Returns:
            The validated password.

        Raises:
            ValueError: If the password is missing or too short.
        """
        if not password:
            raise ValueError("Password is required.")

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters.")

        return password

class UserRegisterResponse:
    """Response schema for user registration."""

    def __init__(
        self,
        message: str,
        success: bool,
        user_id: int | None = None,
    ) -> None:
        """
        Initialize the registration response.

        Args:
            message: Response message.
            success: Whether the registration succeeded.
            user_id: ID of the newly created user, if available.
        """
        self.message = message
        self.success = success
        self.user_id = user_id

    def to_dict(self) -> dict[str, str | bool | int | None]:
        """
        Convert the response object to a dictionary.

        Returns:
            dict: Dictionary representation of the response.
        """
        return {
            "message": self.message,
            "success": self.success,
            "user_id": self.user_id,
        }

if __name__ == "__main__":
    try:
        user = UserRegisterRequest(
            email="akhil@dot.com",
            phone="1234567890",
            password="password"
            )
        print(type(user.phone))
    except ValueError as e:
        print(e)

    response = UserRegisterResponse(
        message = "Student registered successfully.",
        success = True,
        user_id = None
        )
    print(response.to_dict())