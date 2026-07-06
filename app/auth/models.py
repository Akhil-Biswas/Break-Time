"""
app/auth/models.py
    
    Database data models
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int | None = None
    username: str = ""
    email: str = ""
    password_hash: str = ""
    created_at: datetime | None = None