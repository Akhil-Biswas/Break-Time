# API Documentation

User Module

---

## ![POST](https://img.shields.io/badge/POST-007bff?style=for-the-badge&logoColor=white) `/auth/student/register`

### Headers

| Header | Value |
|--------|-------|
| Content-Type | multipart/form-data |

### Request

<details>
<summary><strong>Request Body (Form Data)</strong></summary>

| Field | Type | Required |
|-------|------|----------|
| `f_name` | String | Yes |
| `m_name` | String \| `None` | No |
| `l_name` | String | Yes |
| `email` | String | Yes |
| `password` | String | Yes |
| `phone` | String | Yes |
| `photo` | String \| `None` | No |

Validation

- `email`
    - Must contain @ 
- `phone`
    - Must contain exactly 10 digits.
    - Spaces and hyphens are allowed (e.g., `123-456-7890`, `123 456 7890`).
- `password`
    - Must be at least 8 characters long.

```bash
curl -X POST https://api.akhilbiswas.com/auth/student/register \
  -F "f_name=John" \
  -F "m_name=Michael" \
  -F "l_name=Doe" \
  -F "email=john@example.com" \
  -F "phone=1234567890" \
  -F "password=Password123" \
  -F "photo=@/path/to/photo.jpg"


curl -X POST https://api.akhilbiswas.com/auth/student/register \
  -F "f_name=John" \
  -F "l_name=Doe" \
  -F "email=john@example.com" \
  -F "phone=123-456-7890" \
  -F "password=Password123"
```

</details>

## Responses

<details>
<summary><strong>201 Created</strong></summary>

```json
{
  "message": "Student registered successfully.",
  "success": true,
  "user_id": null
}
```

</details>

<details>
<summary><strong>400 Bad Request</strong></summary>

```json
{
  "error": "Phone number must be 10 digits."
}
```

</details>

---
