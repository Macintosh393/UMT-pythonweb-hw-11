# Contacts Management API (UMT-pythonweb-hw-11)

A contacts management RESTful API built with **FastAPI** and **SQLAlchemy** (using asynchronous queries). This application supports full CRUD operations on contacts, features database migration tracking using **Alembic**, and implements phone number/email validation. It also includes utility endpoints like a database health checker and an upcoming birthdays filter.

## Technologies Used

- **FastAPI**: Modern, asynchronous web framework for building APIs with Python.
- **SQLAlchemy (Async)**: Python SQL toolkit and Object-Relational Mapper (ORM) using `asyncio` for non-blocking database queries.
- **Alembic**: Database migration tool for SQLAlchemy schemas.
- **PostgreSQL / asyncpg**: Relational database storage accessed asynchronously.
- **Pydantic**: Data validation and parsing using Python type annotations.
- **Pydantic Extra Types**: Used for standard validation of phone numbers (`PhoneNumber`) and emails (`EmailStr`).
- **Uvicorn**: Asynchronous Server Gateway Interface (ASGI) server for running the FastAPI application.
- **uv**: Modern, high-performance Python package installer and workspace manager.

---

## Project Structure

```text
umt-pythonweb-hw-08/
├── alembic.ini          # Alembic configuration for migrations
├── main.py              # Main entrypoint to start the FastAPI application
├── pyproject.toml        # Project dependencies and configuration
├── README.md            # Project documentation (this file)
├── uv.lock              # Lockfile for reproducible environment setup
├── migrations/          # Database migration scripts managed by Alembic
└── src/
    ├── api/             # API router endpoints and controllers
    │   ├── contacts.py  # CRUD and filter endpoints for contacts
    │   └── utils.py     # Utility endpoints (e.g. healthchecker)
    ├── conf/            # Configuration modules
    │   └── config.py    # Database connection and environment variables
    ├── database/        # Database connection and models
    │   ├── db.py        # Async database session manager
    │   └── models.py    # SQLAlchemy model definitions
    ├── repository/      # Data Access Object (DAO) / Repository pattern
    │   └── contacts.py  # Database queries and mutations for Contact
    ├── schemas/         # Pydantic schemas for request/response serialization
    │   └── contacts.py  # Contact input, update, and output models
    ├── services/        # Business logic layer
    │   └── contacts.py  # Intermediate services handling repository logic
    └── utils/           # Utility functions and helper modules
        └── birthday_check.py # Helper for checking upcoming birthdays
```

---

## API Endpoints

```text
api/
├── healthchecker
│   └── GET - Verify database connection status and server health
└── contacts
    ├── /
    │   ├── GET - Retrieve all contacts (supports optional filtering and pagination)
    │   └── POST - Create a new contact
    ├── upcoming-birthdays
    │   └── GET - Retrieve contacts with birthdays within the next 7 days
    └── {contact_id}
        ├── GET - Retrieve detailed information for a specific contact
        ├── PUT - Update existing details of a contact
        └── DELETE - Remove a contact from the database
```

### Detailed Endpoint Specifications

| Endpoint                           | Method   | Description                                       | Request/Response Information                                                                                                                                          |
| :--------------------------------- | :------- | :------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/api/healthchecker`               | `GET`    | Verifies PostgreSQL connection.                   | Returns `{"message": "Server is working correctly"}` or `500 Internal Server Error`.                                                                                  |
| `/api/contacts/`                   | `GET`    | Retrieves list of contacts.                       | Query parameters: `first_name` (optional), `last_name` (optional), `email` (optional), `skip` (default 0), `limit` (default 100). Returns array of `ContactResponse`. |
| `/api/contacts/`                   | `POST`   | Creates a new contact.                            | Request body: `ContactModel`. Returns `ContactResponse`.                                                                                                              |
| `/api/contacts/upcoming-birthdays` | `GET`    | Retrieves contacts with birthdays in next 7 days. | Query parameters: `skip` (default 0), `limit` (default 100). Returns array of `ContactResponse`.                                                                      |
| `/api/contacts/{contact_id}`       | `GET`    | Retrieves contact by ID.                          | Path parameter: `contact_id`. Returns `ContactResponse` or `404 Not Found`.                                                                                           |
| `/api/contacts/{contact_id}`       | `PUT`    | Updates contact by ID.                            | Path parameter: `contact_id`. Request body: `ContactUpdate`. Returns `ContactResponse` or `404 Not Found`.                                                            |
| `/api/contacts/{contact_id}`       | `DELETE` | Deletes contact by ID.                            | Path parameter: `contact_id`. Returns the deleted `ContactResponse` or `404 Not Found`.                                                                               |

---

## How to Run

1. **Environment Setup**:
   Ensure you have a PostgreSQL database running and update the `DB_URL` in [src/conf/config.py](file:///c:/Users/maxko/Documents/Projects/Neoversity-homeworks/Python-Git-homeworks/UMT-pythonweb-hw-08/src/conf/config.py) if needed.

2. **Install Dependencies**:

   ```bash
   uv sync
   ```

3. **Run Database Migrations**:

   ```bash
   uv run alembic upgrade head
   ```

4. **Start the Application**:
   ```bash
   uv run python main.py
   ```
   The interactive API documentation will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
