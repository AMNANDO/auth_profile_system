# Auth Profile System

A Django REST Framework (DRF) project for managing user accounts with authentication, permissions, throttling, and account activation/deactivation.

---

## Features

- **User Authentication**: JWT-based authentication for secure API access.
- **Account Management**: Create, retrieve, update, activate, and deactivate accounts.
- **Permissions**: Custom permissions to allow owners and admins to access or modify accounts.
- **Throttling**: Rate limiting for sensitive actions like activating/deactivating accounts.
- **Filtering, Searching, and Ordering**: Easily query accounts with filters, search by name/email/bio, and ordering.
- **Pagination**: Paginated responses for account lists.
- **Custom Exceptions**: Consistent error handling with meaningful messages.
- **API Documentation**: OpenAPI/Swagger documentation using `drf-spectacular`.

---

## Installation

1. Clone the repository:

```bash

git clone https://github.com/AMNANDO/auth_profile_system.git
cd auth_profile_system
```

2. Create a virtual environment and activate it:
```bash

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash

pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```
5. Create a superuser:
```bash

python manage.py createsuperuser
```

6. Run the development server:
```bash

python manage.py runserver
```
## API Endpoints

### Accounts

- **GET /accounts/** – List accounts (supports pagination, search, filter, ordering)
- **GET /accounts/{id}/** – Retrieve account details
- **POST /accounts/** – Create a new account
- **PUT/PATCH /accounts/{id}/** – Update account
- **POST /accounts/{id}/deactivate/** – Deactivate an account
- **POST /accounts/{id}/activate/** – Activate an account

---

## Permissions

- Only account owners or admins can update, delete, activate, or deactivate accounts.
- Authenticated users can list accounts.
- Inactive accounts cannot be retrieved or updated.

---

## Throttling

- Custom throttles for user and anonymous requests.
- Sensitive actions (activate/deactivate) are rate-limited using `ChangeAccountStatusThrottle`.

---

## Running Tests

Run all tests with:

```bash

python manage.py test
```

Documentation

The API documentation is available via Swagger/OpenAPI if drf-spectacular is installed:

Swagger UI: /api/schema/swagger-ui/

ReDoc: /api/schema/redoc/

License

This project is licensed under the MIT License.