# Secure Auth API
[![Tests](https://github.com/reyyan-dev/secure-auth-api/actions/workflows/tests.yml/badge.svg)](https://github.com/reyyan-dev/secure-auth-api/actions/workflows/tests.yml)
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
├── .env.example
├── .gitignore
└── README.md
```
## Local Setup

### 1. Clone the repository

git clone https://github.com/reyyan-dev/secure-auth-api.git
cd secure-auth-api

### 2. Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

cp .env.example .env

Update `.env` with your own secret key and configuration.

### 5. Run the API

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive Swagger documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/auth/register` | Register a new user | No |
| POST | `/auth/login` | Login and receive JWT | No |
| GET | `/auth/me` | Get the authenticated user | Bearer JWT |

## Authentication Flow

1. Register a new user with `/auth/register`.
2. Login using `/auth/login`.
3. Receive a JWT access token.
4. Send the token as a Bearer token.
5. Access protected endpoints such as `/auth/me`.

## Running Tests

Run the complete test suite with:

pytest

The test suite covers:

- User registration
- Successful login
- Invalid password handling
- Protected `/auth/me` endpoint
- Unauthorized access without a token
- Isolated temporary test database per test

## Security

The project demonstrates several common backend security practices:

- Passwords are hashed with bcrypt before storage.
- JWT access tokens are used for authentication.
- Protected endpoints require Bearer authentication.
- Secrets are loaded from environment variables.
- `.env` is excluded from version control.
- Authentication failures return appropriate HTTP status codes.
- Automated tests run through GitHub Actions.

## Future Improvements

Potential production-oriented improvements include:

- Database migrations with Alembic
- Refresh token support
- Email verification
- Password reset functionality
- Rate limiting
- Role-based access control
- Docker containerization
- PostgreSQL support
- Production deployment configuration

## License

This project is provided for portfolio and educational purposes.
