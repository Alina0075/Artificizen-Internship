# Task Management REST API

## Overview

The Task Management REST API is a backend application developed using FastAPI and PostgreSQL. It provides secure user authentication using JSON Web Tokens (JWT) and allows authenticated users to perform CRUD (Create, Read, Update, Delete) operations on their personal tasks.

Each user can register, log in, and manage only their own tasks. The application also supports filtering tasks based on their status.

This project was developed as an End-of-Week Capstone Project during the AI Engineer Internship at Artificizen Pvt. Ltd.

---

## Features

- User Registration
- Secure Password Hashing using bcrypt
- JWT Authentication
- User Login
- Create Tasks
- Retrieve All Tasks
- Retrieve a Single Task
- Update Tasks
- Delete Tasks
- Filter Tasks by Status
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Automated Testing with Pytest

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Programming Language |
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| Passlib (bcrypt) | Password Hashing |
| Python-JOSE | JWT Authentication |
| Uvicorn | ASGI Server |
| Pytest | Testing |
| python-dotenv | Environment Variables |

---

## Project Structure

```
Task-Management-REST-API/
│
├── routers/
│   ├── auth.py
│   └── tasks.py
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_tasks.py
│
├── database.py
├── models.py
├── oauth2.py
├── schema.py
├── utils.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/task-management-rest-api.git

cd task-management-rest-api
```

Replace `<YOUR_USERNAME>` with your GitHub username.

---

### Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost/taskdb

TEST_DATABASE_URL=postgresql://username:password@localhost/taskdb_test

SECRET_KEY=your_secret_key_here

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Database Setup

Create two PostgreSQL databases.

Main database

```
taskdb
```

Testing database

```
taskdb_test
```

---

## Running the Application

Start the FastAPI server.

```bash
uvicorn main:app --reload
```

Application URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

## Authentication

### Register User

**POST**

```
/auth/register
```

Example Request

```json
{
    "username": "alina",
    "password": "password123"
}
```

---

### Login

**POST**

```
/auth/login
```

Returns

```json
{
    "access_token": "<JWT_TOKEN>",
    "token_type": "bearer"
}
```

Use the token in every protected request.

```
Authorization: Bearer <JWT_TOKEN>
```

---

## Task Endpoints

### Create Task

**POST**

```
/tasks/
```

Example

```json
{
    "title": "Complete FastAPI Project",
    "description": "Finish the capstone project",
    "status": "pending",
    "due_date": "2026-08-01"
}
```

---

### Get All Tasks

**GET**

```
/tasks/
```

---

### Filter Tasks

```
GET /tasks/?status=pending
```

Supported values

- pending
- in progress
- done
- due

Status values are automatically normalized before being stored.

---

### Get Single Task

```
GET /tasks/{task_id}
```

---

### Update Task

```
PUT /tasks/{task_id}
```

---

### Delete Task

```
DELETE /tasks/{task_id}
```

Returns

```json
{
    "message": "Task deleted successfully"
}
```

---

## Testing

Run all tests.

```bash
pytest
```

Current Test Result

```
============================ test session starts ============================

platform win32
Python 3.13.5
pytest 9.1.1

collected 9 items

tests/test_auth.py ....                                  [44%]
tests/test_tasks.py .....                                [100%]

======================== 9 passed in approximately 4 seconds ========================
```

---

## Security

- Passwords are hashed using bcrypt before storage.
- JWT authentication secures protected endpoints.
- OAuth2 Bearer Token authentication is implemented.
- Users can only access their own tasks.

---

## Future Improvements

- Pagination
- Task Priorities
- Search by Title
- Sort Tasks
- Refresh Tokens
- Email Notifications
- Docker Support
- Alembic Migrations
- CI/CD Pipeline

---

## API Status

| Module | Status |
|---------|--------|
| Authentication | Complete |
| JWT Authorization | Complete |
| CRUD Operations | Complete |
| Task Filtering | Complete |
| PostgreSQL Integration | Complete |
| Automated Testing | Complete |

---

## Author

**Alina Akhtar**

BS Computer Science

University of Central Punjab

AI Engineer Intern

Artificizen Pvt. Ltd.

GitHub: https://github.com/<YOUR_USERNAME>

LinkedIn: https://linkedin.com/in/<YOUR_LINKEDIN_USERNAME>
