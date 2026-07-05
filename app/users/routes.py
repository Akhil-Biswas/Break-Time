"""
User
"""
from flask import Blueprint

# Create a Blueprint named "user" to organize user-related routes.
user = Blueprint("user", __name__)

@user.route("/profile")
def profile():
    """
    Handle requests to the user profile page.

    Returns:
        str: A simple placeholder response indicating the user profile page.
    """
    return "user profile"