# Authentication Module

This module handles user authentication, registration, profile management, and password recovery.

## Legend

- ✅ = Authentication required
- ❌ = Public route (Guest only)

| Method | Endpoint | Description | Auth | Roles |
| :----: | -------- | ----------- | :--: | ----- |
| ![GET](https://img.shields.io/badge/GET-28a745?style=for-the-badge&logoColor=white) | `/auth/student/register` | Display the student registration page. | ❌ | Guest |
| ![POST](https://img.shields.io/badge/POST-007bff?style=for-the-badge&logoColor=white) | `/auth/student/register` | Register a new student account. | ❌ | Guest |
| ![GET](https://img.shields.io/badge/GET-28a745?style=for-the-badge&logoColor=white) | `/auth/restaurant/register` | Display the restaurant registration page. | ❌ | Guest |
| ![POST](https://img.shields.io/badge/POST-007bff?style=for-the-badge&logoColor=white) | `/auth/restaurant/register` | Register a new restaurant account. | ❌ | Guest |
| ![GET](https://img.shields.io/badge/GET-28a745?style=for-the-badge&logoColor=white) | `/auth/login` | Display the login page. | ❌ | Guest |
| ![POST](https://img.shields.io/badge/POST-007bff?style=for-the-badge&logoColor=white) | `/auth/login` | Authenticate the user and start a session. | ❌ | Guest |
| ![POST](https://img.shields.io/badge/POST-007bff?style=for-the-badge&logoColor=white) | `/auth/logout` | End the current user session. | ✅ | Student, CR, Restaurant, HOD |
| ![GET](https://img.shields.io/badge/GET-28a745?style=for-the-badge&logoColor=white) | `/auth/profile` | Display the authenticated user's profile. | ✅ | Student, CR, Restaurant, HOD |
| ![GET](https://img.shields.io/badge/GET-28a745?style=for-the-badge&logoColor=white) | `/auth/change-password` | Display the change password page. | ✅ | Student, CR, Restaurant, HOD |
| ![POST](https://img.shields.io/badge/POST-007bff?style=for-the-badge&logoColor=white) | `/auth/change-password` | Update the authenticated user's password. | ✅ | Student, CR, Restaurant, HOD |
| ![GET](https://img.shields.io/badge/GET-28a745?style=for-the-badge&logoColor=white) | `/auth/forgot-password` | Display the password recovery page. | ❌ | Guest |
| ![POST](https://img.shields.io/badge/POST-007bff?style=for-the-badge&logoColor=white) | `/auth/forgot-password` | Send a password reset OTP or reset link. | ❌ | Guest |
| ![GET](https://img.shields.io/badge/GET-28a745?style=for-the-badge&logoColor=white) | `/auth/reset-password` | Display the password reset page. | ❌ | Guest |
| ![POST](https://img.shields.io/badge/POST-007bff?style=for-the-badge&logoColor=white) | `/auth/reset-password` | Reset the password using a valid OTP or token. | ❌ | Guest |

---

# Authentication Module File Responsibilities
```text
app/auth/
├── README.md           # documentation
├── __init__.py         #
├── exceptions.py       # Custom exceptions
├── helpers.py          # Utility functions
├── models.py           # Database data models
├── queries.py          # SQL query storage
├── repository.py       # Database access layer
├── routes.py           # HTTP request/response handling
├── schemas.py          # Request and response schemas
└── service.py          # Business logic

1 directory, 10 files

```

## `routes.py`
- **Purpose:** HTTP request/response handling.
- **Responsibilities:**
  - Define Flask routes.
  - Receive HTTP requests.
  - Call schemas and services.
  - Render templates.
  - Return JSON responses or redirects.
- **Should NOT Contain:**
  - SQL queries.
  - Business logic.
  - Password hashing.
  - Validation logic.

## `service.py`
- **Purpose:** Business logic.
- **Responsibilities:**
  - Login and logout.
  - Student registration.
  - Restaurant registration.
  - Password change.
  - Forgot password.
  - Reset password.
  - OTP/token verification.
  - Coordinate repository and helper functions.
- **Should NOT Contain:**
  - Flask routes.
  - HTML rendering.
  - SQL queries.

## `repository.py`
- **Purpose:** Database access layer.
- **Responsibilities:**
  - Execute SQL queries.
  - Pass query parameters.
  - Map database rows to models.
  - Return dataclass objects.
- **Should NOT Contain:**
  - Business logic.
  - Flask code.
  - HTML rendering.

## `queries.py`
- **Purpose:** SQL query storage.
- **Responsibilities:**
  - Store `SELECT` statements.
  - Store `INSERT` statements.
  - Store `UPDATE` statements.
  - Store `DELETE` statements.
  - Store `JOIN` queries.
- **Should NOT Contain:**
  - Database execution code.
  - Business logic.

## `models.py`
- **Purpose:** Database data models.
- **Responsibilities:**
  - Define database entities using `@dataclass`.
  - Define joined query result models.
- **Should NOT Contain:**
  - SQL queries.
  - Validation logic.
  - Business logic.

## `schemas.py`
- **Purpose:** Request and response schemas.
- **Responsibilities:**
  - Validate user input.
  - Define request models.
  - Define response models.
  - Handle serialization/deserialization.
- **Should NOT Contain:**
  - SQL queries.
  - Database access.
  - Business logic.

## `helpers.py`
- **Purpose:** Utility functions.
- **Responsibilities:**
  - Password hashing.
  - Password verification.
  - OTP generation.
  - Token generation.
  - Email helper functions.
  - Session helper functions.
  - Decorators.
  - Reusable utility functions.
- **Should NOT Contain:**
  - SQL queries.
  - Route handlers.
  - Business workflows.

## `exceptions.py`
- **Purpose:** Custom exceptions.
- **Responsibilities:**
  - Define authentication exceptions.
  - Define authorization exceptions.
  - Define validation exceptions.
  - Define application-specific exceptions.
- **Should NOT Contain:**
  - SQL queries.
  - Business logic.
  - Route handling.

## `__init__.py`
- **Purpose:** Package initialization.
- **Responsibilities:**
  - Initialize the package.
  - Export commonly used objects if needed.
- **Should NOT Contain:**
  - Business logic.
  - SQL queries.
  - Route definitions.

## `README.md`
- **Purpose:** Module documentation.
- **Responsibilities:**
  - Describe the module.
  - Document routes.
  - Explain the architecture.
  - Show the folder structure.
  - Provide usage instructions.
- **Should NOT Contain:**
  - Executable application code.

---

# Data Flow

1. Client sends a request.
2. `routes.py` receives the request.
3. `schemas.py` validates the input.
4. `service.py` applies business rules.
5. `repository.py` executes database operations.
6. `queries.py` provides the SQL statements.
7. Database returns data.
8. `repository.py` converts database rows into models from "models.py".
9. `service.py` processes the result.
10. `routes.py` returns the response to the client.

---
