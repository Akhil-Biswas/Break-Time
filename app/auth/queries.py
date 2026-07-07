"""
app/auth/queries.py

SQL query
"""

CREATE_USER = """
INSERT INTO users (
    f_name,
    m_name,
    l_name,
    email,
    password_hash,
    phone,
    photo,
    address,
    role_id,
    is_active
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""
GET_ALL_USER = """
SELECT * FROM users WHERE deleted_at IS NULL
"""

SOFT_DELETE_USER = """
UPDATE users
SET deleted_at = %s
WHERE id = %s
"""

RESTORE_USER = """
UPDATE users
SET deleted_at = NULL
WHERE id = %s
"""

GET_USER_BY_ID = """
SELECT *
FROM users
WHERE id = %s
"""

GET_USER_BY_EMAIL = """
SELECT *
FROM users
WHERE email = %s
"""