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