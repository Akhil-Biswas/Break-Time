# Exception

```txt
Exception
└── AppException
    │
    ├── ClientException (4xx)
    │   │
    │   ├── BadRequestException (400)
    │   │
    │   ├── ValidationException (400/422)
    │   │
    │   ├── UnauthorizedException (401)
    │   │
    │   ├── ForbiddenException (403)
    │   │
    │   ├── NotFoundException (404)
    │   │
    │   ├── ConflictException (409)
    │   │
    │   └── UnprocessableEntityException (422)
    │
    └── ServerException (5xx)
        │
        ├── InternalServerException (500)
        │
        └── DatabaseException
            │
            ├── DatabaseConnectionException (503)
            │
            ├── DatabaseQueryException (500)
            │
            ├── DatabaseTransactionException (500)
            │
            ├── DatabaseIntegrityException (409 or 500)
            │
            └── DatabaseTimeoutException (503 or 504)
```
## Use case

- **`AppException`**
  - Base class for all application-specific exceptions.
  - Used for centralized exception handling and common error properties (message, error code, cause).

- **`BadRequestException`** *(HTTP 400)*
  - Invalid request syntax.
  - Missing required parameters.
  - Invalid query or path parameters.
  - Malformed JSON or request body.

- **`UnauthorizedException`** *(HTTP 401)*
  - Missing authentication token.
  - Invalid or expired JWT/access token.
  - Invalid API key.
  - Authentication failed.

- **`ForbiddenException`** *(HTTP 403)*
  - User is authenticated but lacks permission.
  - Insufficient roles or privileges.
  - Access to restricted resources.

- **`NotFoundException`** *(HTTP 404)*
  - Requested resource does not exist.
  - Invalid resource ID.
  - Requested file or record not found.

- **`ConflictException`** *(HTTP 409)*
  - Duplicate resource creation.
  - Email or username already exists.
  - Version conflict (optimistic locking).
  - Resource is in a conflicting state.

- **`UnprocessableEntityException`** *(HTTP 422)*
  - Request format is valid but violates business rules.
  - Validation failed after parsing.
  - Invalid business logic (e.g., insufficient balance, age restriction).

- **`InternalServerException`** *(HTTP 500)*
  - Unexpected server-side error.
  - Unhandled runtime exception.
  - Unknown application failure.
  - Third-party service failure not mapped to another exception.

- **`DatabaseException`**
  - Base class for all database-related exceptions.
  - Used to group database failures for consistent handling.

- **`DatabaseConnectionException`**
  - Database connection failed.
  - Connection pool exhausted.
  - Database server unavailable.

- **`DatabaseQueryException`**
  - SQL execution failed.
  - ORM query failure.
  - Invalid SQL syntax.
  - Data mapping error.

- **`DatabaseTransactionException`**
  - Transaction commit failed.
  - Transaction rollback failed.
  - Deadlock detected.
  - Transaction aborted.

- **`DatabaseIntegrityException`**
  - Unique constraint violation.
  - Foreign key constraint violation.
  - NOT NULL constraint violation.
  - Check constraint violation.

- **`DatabaseTimeoutException`**
  - Database query timed out.
  - Transaction exceeded timeout.
  - Long-running database operation exceeded configured limits.

# 🌐 HTTP Status Codes

## 🔵 1xx — Informational
| Code | Status |
|:---:|--------|
| ![100](https://img.shields.io/badge/100-blue) | Continue |
| ![101](https://img.shields.io/badge/101-blue) | Switching Protocols |
| ![102](https://img.shields.io/badge/102-blue) | Processing |
| ![103](https://img.shields.io/badge/103-blue) | Early Hints |

---

## 🟢 2xx — Success

| Code | Status |
|:---:|--------|
| ![200](https://img.shields.io/badge/200-green) | OK |
| ![201](https://img.shields.io/badge/201-green) | Created |
| ![202](https://img.shields.io/badge/202-green) | Accepted |
| ![203](https://img.shields.io/badge/203-green) | Non-Authoritative Information |
| ![204](https://img.shields.io/badge/204-green) | No Content |
| ![205](https://img.shields.io/badge/205-green) | Reset Content |
| ![206](https://img.shields.io/badge/206-green) | Partial Content |
| ![207](https://img.shields.io/badge/207-green) | Multi-Status |
| ![208](https://img.shields.io/badge/208-green) | Already Reported |
| ![226](https://img.shields.io/badge/226-green) | IM Used |

---

## 🟡 3xx — Redirection

| Code | Status |
|:---:|--------|
| ![300](https://img.shields.io/badge/300-yellow) | Multiple Choices |
| ![301](https://img.shields.io/badge/301-yellow) | Moved Permanently |
| ![302](https://img.shields.io/badge/302-yellow) | Found |
| ![303](https://img.shields.io/badge/303-yellow) | See Other |
| ![304](https://img.shields.io/badge/304-yellow) | Not Modified |
| ![305](https://img.shields.io/badge/305-yellow) | Use Proxy |
| ![306](https://img.shields.io/badge/306-yellow) | No Longer Used |
| ![307](https://img.shields.io/badge/307-yellow) | Temporary Redirect |
| ![308](https://img.shields.io/badge/308-yellow) | Permanent Redirect |

---

## 🔴 4xx — Client Errors

| Code | Status |
|:---:|--------|
| ![400](https://img.shields.io/badge/400-red) | Bad Request |
| ![401](https://img.shields.io/badge/401-red) | Unauthorized |
| ![402](https://img.shields.io/badge/402-red) | Payment Required |
| ![403](https://img.shields.io/badge/403-red) | Forbidden |
| ![404](https://img.shields.io/badge/404-red) | Not Found |
| ![405](https://img.shields.io/badge/405-red) | Method Not Allowed |
| ![406](https://img.shields.io/badge/406-red) | Not Acceptable |
| ![407](https://img.shields.io/badge/407-red) | Proxy Authentication Required |
| ![408](https://img.shields.io/badge/408-red) | Request Timeout |
| ![409](https://img.shields.io/badge/409-red) | Conflict |
| ![410](https://img.shields.io/badge/410-red) | Gone |
| ![411](https://img.shields.io/badge/411-red) | Length Required |
| ![412](https://img.shields.io/badge/412-red) | Precondition Failed |
| ![413](https://img.shields.io/badge/413-red) | Payload Too Large |
| ![414](https://img.shields.io/badge/414-red) | URI Too Long |
| ![415](https://img.shields.io/badge/415-red) | Unsupported Media Type |
| ![416](https://img.shields.io/badge/416-red) | Range Not Satisfiable |
| ![417](https://img.shields.io/badge/417-red) | Expectation Failed |
| ![421](https://img.shields.io/badge/421-red) | Misdirected Request |
| ![422](https://img.shields.io/badge/422-red) | Unprocessable Entity |
| ![423](https://img.shields.io/badge/423-red) | Locked |
| ![424](https://img.shields.io/badge/424-red) | Failed Dependency |
| ![425](https://img.shields.io/badge/425-red) | Too Early |
| ![426](https://img.shields.io/badge/426-red) | Upgrade Required |
| ![428](https://img.shields.io/badge/428-red) | Precondition Required |
| ![429](https://img.shields.io/badge/429-red) | Too Many Requests |
| ![431](https://img.shields.io/badge/431-red) | Request Header Fields Too Large |
| ![451](https://img.shields.io/badge/451-red) | Unavailable For Legal Reasons |

---

## 🟠 5xx — Server Errors

| Code | Status |
|:---:|--------|
| ![500](https://img.shields.io/badge/500-orange) | Internal Server Error |
| ![501](https://img.shields.io/badge/501-orange) | Not Implemented |
| ![502](https://img.shields.io/badge/502-orange) | Bad Gateway |
| ![503](https://img.shields.io/badge/503-orange) | Service Unavailable |
| ![504](https://img.shields.io/badge/504-orange) | Gateway Timeout |
| ![505](https://img.shields.io/badge/505-orange) | HTTP Version Not Supported |
| ![507](https://img.shields.io/badge/507-orange) | Insufficient Storage |
| ![508](https://img.shields.io/badge/508-orange) | Loop Detected |
| ![510](https://img.shields.io/badge/510-orange) | Not Extended |
| ![511](https://img.shields.io/badge/511-orange) | Network Authentication Required |

## `mysql-connector-python` Exceptions

[`mysql-connector-python` Docs ](https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors.html)

```txt
Exception
└── Error
    ├── Warning
    ├── InterfaceError
    └── DatabaseError
        ├── DataError
        ├── OperationalError
        ├── IntegrityError
        ├── InternalError
        ├── ProgrammingError
        ├── NotSupportedError
        └── PoolError
```
### MySQL Connector Exception Mapping

| MySQL Connector Exception | Description | Application Exception | HTTP Status |
|---------------------------|-------------|-----------------------|-------------|
| `Warning` | Non-fatal warning generated by the database driver. Typically logged and does not interrupt execution. | _Not Mapped (Log Only)_ | N/A |
| `InterfaceError` | Errors related to the database interface, such as connection establishment or communication failures. | `DatabaseConnectionException` | **![503](https://img.shields.io/badge/503-orange) Service Unavailable** |
| `DataError` | Invalid or out-of-range data values (e.g., numeric overflow, data truncation). | `DatabaseQueryException` | **![500](https://img.shields.io/badge/500-orange) Internal Server Error** |
| `OperationalError` *(Connection Failure)* | Database server unavailable, lost connection, or network-related errors. | `DatabaseConnectionException` | **![503](https://img.shields.io/badge/503-orange) Service Unavailable** |
| `OperationalError` *(Timeout)* | Database operation exceeded the configured timeout. | `DatabaseTimeoutException` | **![503](https://img.shields.io/badge/503-orange) Service Unavailable** or **![504](https://img.shields.io/badge/504-orange) Gateway Timeout** |
| `OperationalError` *(Transaction Failure)* | Transaction failed due to deadlock or rollback conditions. | `DatabaseTransactionException` | **![500](https://img.shields.io/badge/500-orange) Internal Server Error** |
| `OperationalError` *(Other)* | Other operational failures not covered by a specific category. | `DatabaseQueryException` | **![500](https://img.shields.io/badge/500-orange) Internal Server Error** |
| `IntegrityError` | Constraint violations such as duplicate keys, unique constraints, or foreign key violations. | `DatabaseIntegrityException` | **![409](https://img.shields.io/badge/409-red) Conflict** |
| `InternalError` | Internal database or driver errors encountered during execution. | `DatabaseQueryException` | **![500](https://img.shields.io/badge/500-orange) Internal Server Error** |
| `ProgrammingError` | SQL syntax errors, invalid table names, invalid column names, or incorrect query structure. | `DatabaseQueryException` | **![500](https://img.shields.io/badge/500-orange) Internal Server Error** |
| `NotSupportedError` | Attempted to use an unsupported database feature or operation. | `DatabaseQueryException` | **![500](https://img.shields.io/badge/500-orange) Internal Server Error** |
| `PoolError` | Connection pool is exhausted or unavailable. | `DatabaseConnectionException` | **![503](https://img.shields.io/badge/503-orange) Service Unavailable** |
| `DatabaseError` *(Fallback)* | Generic database error not handled by a more specific exception type. | `DatabaseException` | **![500](https://img.shields.io/badge/500-orange) Internal Server Error** |
| `Error` *(Fallback)* | Base class for all MySQL Connector exceptions. Used only as a final fallback. | `DatabaseException` | **![500](https://img.shields.io/badge/500-orange) Internal Server Error** |

<details>
<summary><strong>Mapping Summary</strong></summary>

- `DatabaseConnectionException`
    - `InterfaceError`
    - `OperationalError` *(Connection Failure)*
    - `PoolError`

- `DatabaseTimeoutException`
    - `OperationalError` *(Timeout)*

- `DatabaseTransactionException`
    - `OperationalError` *(Transaction Failure)*

- `DatabaseIntegrityException`
    - `IntegrityError`

- `DatabaseQueryException`
    - `DataError`
    - `ProgrammingError`
    - `InternalError`
    - `NotSupportedError`
    - `OperationalError` *(Other)*

- `DatabaseException` *(Fallback)*
    - `DatabaseError`
    - `Error`

- Not Mapped
    - `Warning` *(Logged only; no application exception is thrown.)*

</details>
