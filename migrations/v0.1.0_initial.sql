-- =====================================================================
-- College Canteen Management System Database Schema
-- Version : 0.1.0
-- Date    : 5 Jul 2026
-- =====================================================================
-- Roles Table
CREATE TABLE roles (
    -- Unique identifier for each role
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Name of the role
    -- Examples: HOD, Restaurant, Student
    name VARCHAR(50) NOT NULL UNIQUE
);

-- =====================================================================
-- Users Table
-- Required: Roles Table
CREATE TABLE users (
    -- Unique identifier for each user
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- User's first name
    f_name VARCHAR(50) NOT NULL,

    -- User's middle name (optional)
    m_name VARCHAR(50) NULL,

    -- User's last name
    l_name VARCHAR(50) NOT NULL,

    -- User's email address (used for login)
    email VARCHAR(150) NOT NULL UNIQUE,

    -- Hashed password (never store plain text passwords)
    password_hash VARCHAR(255) NOT NULL,

    -- User's phone number
    -- Stored as VARCHAR to support country codes
    phone VARCHAR(20) NOT NULL,

    -- Profile photo path or URL
    photo VARCHAR(255) NULL,

    -- User's address
    address VARCHAR(255) NULL,

    -- Reference to the user's role
    role_id INT NOT NULL,

    -- Indicates whether the account is active
    is_active BOOLEAN NOT NULL DEFAULT TRUE,

    -- Timestamp when the record was created
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- Timestamp automatically updated whenever the record changes
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    -- Soft delete timestamp (NULL means not deleted)
    deleted_at DATETIME NULL,

    -- Foreign key linking to the roles table
    CONSTRAINT fk_users_role
        FOREIGN KEY (role_id)
        REFERENCES roles(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- =====================================================================
-- Departments Table
CREATE TABLE departments (
    -- Unique identifier for each department
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Name of the department
    name VARCHAR(150) NOT NULL
);

-- =====================================================================
-- Sections Table
CREATE TABLE sections (
    -- Unique identifier for each section
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Section name
    -- Examples: A, B, C
    name VARCHAR(50) NOT NULL,

    -- Department to which this section belongs
    department_id INT NOT NULL,

    -- Foreign key linking to the departments table
    CONSTRAINT fk_sections_department
        FOREIGN KEY (department_id)
        REFERENCES departments(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    
    -- composite unique constraint:
        -- CSE   A
        -- CSE   A  (Not allowed)
    CONSTRAINT uk_sections_department_name
    UNIQUE (department_id, name)
);

-- =====================================================================
-- Genders Table
CREATE TABLE genders (
    -- Unique identifier for each gender
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Gender name
    -- Examples: Male, Female, Other
    name VARCHAR(20) NOT NULL UNIQUE
);

-- =====================================================================
-- Student Details Table
CREATE TABLE student_details (
    -- References the user account (1-to-1 relationship)
    user_id INT PRIMARY KEY,

    -- Student roll number
    -- Example: 21CSE045
    roll_number VARCHAR(50) NOT NULL UNIQUE,

    -- Department in which the student is enrolled
    department_id INT NOT NULL,

    -- Current semester (must be greater than 0)
    semester TINYINT NOT NULL CHECK (semester BETWEEN 1 AND 8),

    -- Section assigned to the student
    section_id INT NOT NULL,

    -- Indicates whether the student is a Class Representative (CR)
    is_cr BOOLEAN NOT NULL DEFAULT FALSE,

    -- Student's gender
    gender_id INT NOT NULL,

    -- One-to-one relationship with users table
    CONSTRAINT fk_student_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    -- Department reference
    CONSTRAINT fk_student_department
        FOREIGN KEY (department_id)
        REFERENCES departments(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    -- Section reference
    CONSTRAINT fk_student_section
        FOREIGN KEY (section_id)
        REFERENCES sections(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    -- Gender reference
    CONSTRAINT fk_student_gender
        FOREIGN KEY (gender_id)
        REFERENCES genders(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- =====================================================================
-- HOD Details Table
CREATE TABLE hod_details (
    -- References the user account (1-to-1 relationship)
    user_id INT PRIMARY KEY ,

    -- Department managed by the HOD
    department_id INT NOT NULL UNIQUE,

    -- One-to-one relationship with users table
    CONSTRAINT fk_hod_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    -- Department reference
    CONSTRAINT fk_hod_department
        FOREIGN KEY (department_id)
        REFERENCES departments(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- =====================================================================
-- Restaurant Details Table

CREATE TABLE restaurant_details (
    -- References the user account (1-to-1 relationship)
    user_id INT PRIMARY KEY,

    -- Restaurant name
    restaurant_name VARCHAR(150) NOT NULL,

    -- Daily opening time
    opening_time TIME NOT NULL,

    -- Daily closing time
    closing_time TIME NOT NULL,

    -- Indicates whether the restaurant is currently open
    is_open BOOLEAN NOT NULL DEFAULT TRUE,

    -- One-to-one relationship with users table
    CONSTRAINT fk_restaurant_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    -- Ensure the opening and closing times are different
    CONSTRAINT chk_restaurant_time
        CHECK (opening_time <> closing_time)
);