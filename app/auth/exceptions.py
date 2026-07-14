"""
app/auth/exceptions.py

Authentication module exceptions.

Defines custom exceptions for authentication, authorization, account
management, password recovery, and permission-related business errors.
These exceptions are built on top of the application's core exception
hierarchy.
"""
from app.core.exceptions import (
    ConflictException,
    NotFoundException,
    UnauthorizedException,
    ForbiddenException,
)


# ============================================================================
# Conflict (409)
# ============================================================================

class UserAlreadyExistsException(ConflictException):
    """Raised when a user already exists."""
    message: str = "User already exists"


class EmailAlreadyExistsException(UserAlreadyExistsException):
    """Raised when the supplied email address is already registered."""
    message: str = "Email address is already registered"


class PhoneAlreadyExistsException(UserAlreadyExistsException):
    """Raised when the supplied phone number is already registered."""
    message: str = "Phone number is already registered"


class PasswordMismatchException(ConflictException):
    """Raised when the new password and its confirmation do not match."""
    message: str = "Passwords do not match"


class PasswordReuseException(ConflictException):
    """Raised when the new password matches a previously used password."""
    message: str = "New password cannot be the same as a previously used password"


# ============================================================================
# Not Found (404)
# ============================================================================

class UserNotFoundException(NotFoundException):
    """Raised when the requested user cannot be found."""
    message: str = "User not found"


# ============================================================================
# Unauthorized (401)
# ============================================================================

class InvalidCredentialsException(UnauthorizedException):
    """Raised when authentication fails because the provided credentials are invalid."""
    message: str = "Invalid credentials"


class AccountNotVerifiedException(UnauthorizedException):
    """Raised when a user attempts to authenticate before verifying their account."""
    message: str = "Account is not verified. Please verify your account first"


class InvalidOtpException(UnauthorizedException):
    """Raised when an invalid one-time password (OTP) is provided."""
    message: str = "Invalid OTP"


class OtpExpiredException(UnauthorizedException):
    """Raised when the submitted OTP has expired."""
    message: str = "OTP has expired. Please request a new one"


class InvalidTokenException(UnauthorizedException):
    """Raised when an authentication or password reset token is invalid or malformed."""
    message: str = "Invalid token"


class TokenExpiredException(UnauthorizedException):
    """Raised when an authentication or password reset token has expired."""
    message: str = "Token has expired. Please request a new one"


# ============================================================================
# Forbidden (403)
# ============================================================================

class PermissionDeniedException(ForbiddenException):
    """Raised when an authenticated user attempts an action they are not permitted to perform."""
    message: str = "You do not have permission to perform this action"


class InsufficientPrivilegesException(PermissionDeniedException):
    """Raised when the user's role or privileges are insufficient to perform the requested operation."""
    message: str = "You do not have sufficient privileges to perform this action"


class AccountDisabledException(ForbiddenException):
    """Raised when an account has been disabled by an administrator."""
    message: str = "Your account has been disabled. Please contact support"


class AccountLockedException(ForbiddenException):
    """Raised when an account has been temporarily locked due to security policies."""
    message: str = "Your account has been temporarily locked. Please try again later"
