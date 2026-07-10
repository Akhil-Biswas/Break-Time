# API Response Standard

## Overview

This document defines the standard JSON response format used by all API endpoints.

Every API response **must** follow one of the formats described below.

---

# Success Response

```json
{
  "success": true,
  "data": {},
  "error": null,
  "metadata": null
}
```

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `success` | `boolean` | Yes | Indicates whether the request was successful. |
| `data` | `object \| array \| any \| null` | Yes | The response payload. |
| `error` | `object \| null` | Yes | Always `null` for successful responses. |
| `metadata` | `object \| null` | Yes | Optional response metadata. Use `null` when not applicable. |

### Rules

- `success` must be `true`.
- `data` contains the response payload.
- `error` must be `null`.

---

# Error Response

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message.",
    "details": null
  },
  "metadata": null
}
```

## Error Object

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `code` | `string` | Yes | Machine-readable error code. |
| `message` | `string` | Yes | Human-readable error description. |
| `details` | `object \| array \| string \| null` | Yes | Additional diagnostic information. Use `null` when unavailable. |

### Rules

- `success` must be `false`.
- `data` must be `null`.
- `error` must be present.
- `error.code` is required.
- `error.message` is required.
- `error.details` is required.

---

# Metadata

The `metadata` field contains optional information that is not part of the primary response.

Examples include:

- Pagination
- Timestamp
- Request ID
- Processing time

If no metadata is available:

```json
{
  "metadata": null
}
```

Example:

```json
{
  "metadata": {
    "request_id": "5f92f3f4",
    "timestamp": "2026-07-08T12:00:00Z"
  }
}
```

---

# Standard Error Codes

| Code | Description |
|------|-------------|
| `BAD_REQUEST` | Invalid request syntax or parameters. |
| `VALIDATION_ERROR` | Request validation failed. |
| `UNAUTHORIZED` | Authentication required or failed. |
| `FORBIDDEN` | Permission denied. |
| `NOT_FOUND` | Resource not found. |
| `CONFLICT` | Resource conflict. |
| `RATE_LIMIT_EXCEEDED` | Too many requests. |
| `INTERNAL_SERVER_ERROR` | Unexpected server error. |

---

# Best Practices

- Return **either** `data` **or** `error`, never both.
- Always include all top-level fields.
- Keep error messages concise and user-friendly.
- Use consistent error codes throughout the application.
- Include `details` only when additional information is useful.
- Set unused optional fields to `null`.

---

# Examples

## Successful Response

```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "Ram"
  },
  "error": null,
  "metadata": null
}
```

## Error Response

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "UNAUTHORIZED",
    "message": "You can't access this resource.",
    "details": null
  },
  "metadata": null
}
```
