from dataclasses import dataclass
from datetime import datetime, time
from typing import Optional


# ==========================================================
# Roles
# ==========================================================

@dataclass
class Role:
    id: Optional[int] = None
    name: str = ""


# ==========================================================
# Users
# ==========================================================

@dataclass
class User:
    id: Optional[int] = None

    f_name: str = ""
    m_name: Optional[str] = None
    l_name: str = ""

    email: str = ""
    password_hash: str = ""

    phone: str = ""
    photo: Optional[str] = None
    address: Optional[str] = None

    role_id: int = 0

    is_active: bool = True

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


# ==========================================================
# Departments
# ==========================================================

@dataclass
class Department:
    id: Optional[int] = None
    name: str = ""


# ==========================================================
# Sections
# ==========================================================

@dataclass
class Section:
    id: Optional[int] = None
    name: str = ""
    department_id: int = 0


# ==========================================================
# Genders
# ==========================================================

@dataclass
class Gender:
    id: Optional[int] = None
    name: str = ""


# ==========================================================
# Student Details
# ==========================================================

@dataclass
class StudentDetails:
    user_id: int
    roll_number: str
    department_id: int
    semester: int
    section_id: int
    is_cr: bool = False
    gender_id: int = 0


# ==========================================================
# HOD Details
# ==========================================================

@dataclass
class HODDetails:
    user_id: int
    department_id: int


# ==========================================================
# Restaurant Details
# ==========================================================

@dataclass
class RestaurantDetails:
    user_id: int
    restaurant_name: str
    opening_time: time
    closing_time: time
    is_open: bool = True