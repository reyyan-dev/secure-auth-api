# Secure Auth API

A production-style authentication backend built with Python and FastAPI.

This project demonstrates secure user registration, password hashing, JWT-based authentication, protected API routes, database integration, and automated testing.

## Features

- User registration
- Email and username uniqueness validation
- Secure password hashing with bcrypt
- User login with JWT access tokens
- Protected `/auth/me` endpoint
- Token expiration
- SQLAlchemy ORM
- SQLite database
- Pydantic request/response validation
- Automated API tests with pytest
- Interactive Swagger API documentation
- Environment-based configuration

## Tech Stack

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- PyJWT
- Passlib
- bcrypt
- pytest
- Uvicorn

## Project Structure

```text
secure-auth-api/
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   └── dependencies.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   └── database.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── auth.py
│   ├── services/
│   │   ├── jwt.py
│   │   └── security.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_auth.py
├── .env
├── .gitignore
└── README.md

