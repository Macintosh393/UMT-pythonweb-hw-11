# Contacts Management API (UMT-pythonweb-hw-11)

A feature-rich contacts management RESTful API built with **FastAPI** and **SQLAlchemy** (using asynchronous queries). This application supports full CRUD operations on contacts, user authentication with email verification, avatar uploads, and JWT-based authorization. It includes database migration tracking with **Alembic**, phone number/email validation, and rate limiting.

## Key Features

- ✅ **User Authentication** - Register and login with JWT tokens
- ✅ **Email Verification** - Send confirmation emails before account activation
- ✅ **Avatar Upload** - Upload and manage user avatars via Cloudinary
- ✅ **Password Hashing** - Secure bcrypt password hashing with rate limiting
- ✅ **Rate Limiting** - Protect endpoints with slowapi rate limiting
- ✅ **Full CRUD Contacts** - Create, read, update, delete contacts per user
- ✅ **Birthday Filtering** - Find contacts with upcoming birthdays
- ✅ **Async Database** - PostgreSQL with async queries for high performance
- ✅ **Database Migrations** - Alembic for schema versioning

## Technologies Used

- **FastAPI**: Modern, asynchronous web framework for building APIs with Python.
- **SQLAlchemy (Async)**: Python SQL toolkit and Object-Relational Mapper (ORM) using `asyncio` for non-blocking database queries.
- **Alembic**: Database migration tool for SQLAlchemy schemas.
- **PostgreSQL / asyncpg**: Relational database storage accessed asynchronously.
- **Pydantic & Pydantic Settings**: Data validation and configuration management using Python type annotations.
- **Pydantic Extra Types**: Validation for phone numbers (`PhoneNumber`) and emails (`EmailStr`).
- **Passlib & Bcrypt**: Secure password hashing and verification.
- **Python-Jose**: JWT token creation and validation.
- **FastAPI-Mail**: Email sending with template support.
- **Cloudinary**: Cloud-based image storage for avatar uploads.
- **SlowAPI**: Rate limiting middleware for FastAPI.
- **Uvicorn**: Asynchronous Server Gateway Interface (ASGI) server for running the FastAPI application.
- **uv**: Modern, high-performance Python package installer and workspace manager.

---

## Project Structure

```text
UMT-pythonweb-hw-11/
├── alembic.ini          # Alembic configuration for migrations
├── main.py              # Main entrypoint to start the FastAPI application
├── pyproject.toml        # Project dependencies and configuration
├── README.md            # Project documentation (this file)
├── .env.example         # Environment variables template
├── migrations/          # Database migration scripts managed by Alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions/        # Migration version files
└── src/
    ├── api/             # API router endpoints and controllers
    │   ├── auth.py      # Authentication endpoints (register, login)
    │   ├── users.py     # User endpoints (get profile, update avatar)
    │   ├── contacts.py  # CRUD and filter endpoints for contacts
    │   └── utils.py     # Utility endpoints
    ├── conf/            # Configuration modules
    │   └── config.py    # Database and service configuration from env vars
    ├── database/        # Database connection and models
    │   ├── db.py        # Async database session manager
    │   └── models.py    # SQLAlchemy model definitions (User, Contact)
    ├── repository/      # Data Access Object (DAO) / Repository pattern
    │   ├── contacts.py  # Database queries for contacts
    │   └── users.py     # Database queries for users
    ├── schemas/         # Pydantic schemas for request/response serialization
    │   ├── contacts.py  # Contact models
    │   ├── users.py     # User models
    │   └── tokens.py    # Token models
    ├── services/        # Business logic layer
    │   ├── auth.py      # Authentication, JWT, and password services
    │   ├── users.py     # User business logic
    │   ├── contacts.py  # Contact business logic
    │   ├── email.py     # Email sending service
    │   └── upload_file.py # File upload service (Cloudinary)
    ├── utils/           # Utility functions and helper modules
    │   └── birthday_check.py # Helper for checking upcoming birthdays
    └── templates/       # Email templates
        └── verify_email.html # Email verification template
```

---

## API Endpoints

### Authentication Routes (`/api/auth`)

| Endpoint                          | Method | Description                           | Auth Required |
| :-------------------------------- | :----- | :------------------------------------ | :------------ |
| `/api/auth/register`              | `POST` | Register a new user account           | No            |
| `/api/auth/login`                 | `POST` | Login and get JWT access token        | No            |
| `/api/auth/confirm_email/{token}` | `GET`  | Confirm email with verification token | No            |
| `/api/auth/request_email`         | `POST` | Request email verification (resend)   | No            |

### Users Routes (`/api/users`)

| Endpoint            | Method  | Description               | Auth Required |
| :------------------ | :------ | :------------------------ | :------------ |
| `/api/users/me`     | `GET`   | Get current user profile  | Yes           |
| `/api/users/avatar` | `PATCH` | Upload/update user avatar | Yes           |

### Contacts Routes (`/api/contacts`)

| Endpoint                           | Method   | Description                                | Auth Required |
| :--------------------------------- | :------- | :----------------------------------------- | :------------ |
| `/api/contacts/`                   | `GET`    | List all user contacts with pagination     | Yes           |
| `/api/contacts/`                   | `POST`   | Create a new contact                       | Yes           |
| `/api/contacts/{contact_id}`       | `GET`    | Get contact details by ID                  | Yes           |
| `/api/contacts/{contact_id}`       | `PUT`    | Update contact information                 | Yes           |
| `/api/contacts/{contact_id}`       | `DELETE` | Delete a contact                           | Yes           |
| `/api/contacts/upcoming-birthdays` | `GET`    | Get contacts with birthdays in next 7 days | Yes           |

### Utility Routes (`/api`)

| Endpoint             | Method | Description               |
| :------------------- | :----- | :------------------------ |
| `/api/healthchecker` | `GET`  | Check database connection |

---

## Setup Instructions

### Prerequisites

- Python 3.14+ (or uv without Python installed)
- Docker & Docker Compose (for containerized setup)
- Cloudinary account (for avatar uploads)
- SMTP email service account (Gmail, Meta, etc.)

---

## Quick Start with Docker Compose

The **easiest way** to run the entire application (with PostgreSQL) is using Docker Compose:

### 1. Clone and Setup

```bash
git clone <repository-url>
cd UMT-pythonweb-hw-11
cp .env.example .env
```

### 2. Configure `.env` File

Edit `.env` with your configuration (see **Environment Variables** section below). Minimum example:

```env
# PostgreSQL Configuration
POSTGRES_DB=contacts_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
POSTGRES_HOST=postgres

# Database URL (use 'postgres' for Docker Compose hostname)
DB_URL=postgresql+asyncpg://postgres:postgres@postgres:5432/contacts_db

# JWT Configuration
JWT_SECRET=your-super-secret-key-change-this-to-something-secure
JWT_ALGORITHM=HS256
JWT_EXPIRATION_SECONDS=3600

# Email Configuration
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-app-password
MAIL_FROM=your-email@example.com
MAIL_SERVER=smtp.example.com
MAIL_PORT=465

# Cloudinary Configuration
CLD_NAME=your-cloudinary-name
CLD_API_KEY=your-cloudinary-api-key
CLD_API_SECRET=your-cloudinary-api-secret
```

### 3. Start Services with Docker Compose

```bash
# Start PostgreSQL database in background
docker compose up -d

# Wait a moment for PostgreSQL to initialize
sleep 5

# Install dependencies and run migrations
uv sync
uv run alembic upgrade head

# Start the FastAPI application
uv run python main.py
```

**Interactive API documentation:**

- Swagger UI: `http://localhost:8000/docs`

---

## Environment Variables Guide

### PostgreSQL Database Configuration

```env
# PostgreSQL server host
# Use 'postgres' for Docker Compose, 'localhost' for local setup
POSTGRES_HOST=postgres

# PostgreSQL server port (default: 5432)
POSTGRES_PORT=5432

# Database name to create and use
POSTGRES_DB=contacts_db

# PostgreSQL superuser
POSTGRES_USER=postgres

# PostgreSQL password
POSTGRES_PASSWORD=postgres

# Full SQLAlchemy database URL
# Format: postgresql+asyncpg://user:password@host:port/database
DB_URL=postgresql+asyncpg://postgres:postgres@postgres:5432/contacts_db
```

### JWT Authentication Configuration

```env
# Secret key for signing and verifying JWT tokens
# IMPORTANT: Use a strong random string (at least 32 characters)
# You can generate one with: python -c "import secrets; print(secrets.token_urlsafe(32))"
JWT_SECRET=your-super-secret-key-at-least-32-characters-long

# JWT algorithm (HS256 is standard and recommended)
JWT_ALGORITHM=HS256

# Token expiration time in seconds
# Default: 3600 (1 hour)
# Example: 86400 for 24 hours
JWT_EXPIRATION_SECONDS=3600
```

### Email Configuration (SMTP)

```env
# Email account username/address
MAIL_USERNAME=your-email@example.com

# Email account password or app-specific password
# For Gmail: Generate an App Password
# For Office 365: Use your account password or app password
MAIL_PASSWORD=your-app-password

# Sender email address (usually same as MAIL_USERNAME)
MAIL_FROM=your-email@example.com

# SMTP server address
# Common options:
#   - Gmail: smtp.gmail.com
#   - Office 365: smtp.office365.com
#   - SendGrid: smtp.sendgrid.net
#   - Meta/Ukraine: smtp.meta.ua
MAIL_SERVER=smtp.gmail.com

# SMTP server port
# 465 = SSL/TLS encryption
# 587 = STARTTLS encryption
MAIL_PORT=465

# Display name for outgoing emails
MAIL_FROM_NAME=Contacts API Service

# Use STARTTLS encryption (True for port 587, False for port 465)
MAIL_STARTTLS=False

# Use SSL/TLS encryption (True for port 465, False for port 587)
MAIL_SSL_TLS=True

# Whether to authenticate with MAIL_USERNAME and MAIL_PASSWORD
USE_CREDENTIALS=True

# Validate SSL certificates (set False only for testing with self-signed certs)
VALIDATE_CERTS=True
```

**Common SMTP Server Examples:**

```env
# Gmail (with App Password)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_STARTTLS=True
MAIL_SSL_TLS=False

# Office 365 / Outlook
MAIL_SERVER=smtp.office365.com
MAIL_PORT=587
MAIL_STARTTLS=True
MAIL_SSL_TLS=False

# SendGrid
MAIL_USERNAME=apikey
MAIL_PASSWORD=SG.your_sendgrid_api_key
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_STARTTLS=True
MAIL_SSL_TLS=False
```

### Cloudinary Image Upload Configuration

```env
# Your Cloudinary cloud name
# Get from: https://cloudinary.com/console/settings/account
CLD_NAME=your-cloud-name

# Cloudinary API Key
# Get from: https://cloudinary.com/console/settings/api-keys
CLD_API_KEY=your-api-key-from-dashboard

# Cloudinary API Secret
# Get from: https://cloudinary.com/console/settings/api-keys
# IMPORTANT: Keep this secret and never commit it to version control
CLD_API_SECRET=your-api-secret-from-dashboard
```

[Get your Cloudinary credentials →](https://cloudinary.com/console/)

---

## Usage Examples

### Register a New User

```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password123"
  }'
```

### Login

```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john_doe&password=secure_password123"
```

### Get User Profile (Requires JWT Token)

```bash
curl -X GET http://localhost:8000/api/users/me \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### Create a Contact

```bash
curl -X POST http://localhost:8000/api/contacts/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane@example.com",
    "phone": "+1234567890",
    "date_of_birth": "1990-01-15"
  }'
```

---

## Development

### Database Migrations

Create a new migration after model changes:

```bash
uv run alembic revision --autogenerate -m "Description of changes"
uv run alembic upgrade head
```

### Code Formatting

```bash
# Format code with Black
uv run black src/

# Check with Pylint
uv run pylint src/
```

---

## Project Structure Details

### Authentication Flow

1. User registers with email and password
2. Password hashed with bcrypt
3. Confirmation email sent with JWT token
4. User clicks link to confirm email
5. User logs in and receives access token
6. All subsequent requests require valid JWT token

### Database Models

- **User**: Stores user account information, hashed passwords, and email confirmation status
- **Contact**: Stores contact details, linked to a specific user via `user_id`

### Rate Limiting

- `/api/users/me` endpoint: 10 requests per minute
- Uses IP address for rate limit key

---

## API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI (OpenAPI)**: `http://localhost:8000/docs`

These provide full endpoint documentation with request/response schemas and allow you to test endpoints directly.

---

## Common Issues & Solutions

### Database Connection Error

Ensure PostgreSQL is running and `DB_URL` is correctly configured in `.env`

### Email Sending Failed

Check SMTP credentials and ensure the email provider allows app passwords (e.g., Gmail)

### Cloudinary Upload Error

Verify `CLD_NAME`, `CLD_API_KEY`, and `CLD_API_SECRET` are set correctly in `.env`

---

```
The interactive API documentation will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
```
