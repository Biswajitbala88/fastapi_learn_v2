# FastAPI Todo App

A Todo API built with FastAPI, MySQL, SQLAlchemy, JWT Authentication, and Pydantic.

## Features

* User Registration
* User Login
* JWT Authentication
* Create Tasks
* Update Tasks
* Delete Tasks
* User-specific Tasks
* MySQL Database
* SQLAlchemy ORM

---

# Requirements

* Python 3.13+
* MySQL
* UV
* Git

---

# Clone Project

```bash
git clone <repository-url>
cd fastapi_learn_v2
```

---

# Install UV

If UV is not installed:

```bash
pip install uv
```

Verify:

```bash
uv --version
```

---

# Install Dependencies

```bash
uv sync
```

This installs all packages defined in:

```text
pyproject.toml
uv.lock
```

---

# Create Database

Login to MySQL:

```sql
CREATE DATABASE todo_app;
```

Verify:

```sql
SHOW DATABASES;
```

---

# Configure Database

Open:

```text
app/database.py
```

Update connection string:

```python
DATABASE_URL = "mysql+pymysql://root:password@127.0.0.1:3306/todo_app"
```

Examples:

### No Password

```python
DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/todo_app"
```

### Password Protected

```python
DATABASE_URL = "mysql+pymysql://root:secret@127.0.0.1:3306/todo_app"
```

---

# Project Structure

```text
fastapi_learn_v2/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── task.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── task_schema.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   └── task.py
│   │
│   ├── dependencies/
│   │   └── auth.py
│   │
│   └── utils/
│       ├── security.py
│       └── jwt_handler.py
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Run Application

```bash
uv run uvicorn app.main:app --reload
```

Custom Port:

```bash
uv run uvicorn app.main:app --reload --port 9000
```

---

# API Documentation

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Authentication Flow

## Register

```http
POST /auth/register
```

Request:

```json
{
    "name": "Biswajit",
    "email": "biswajit@example.com",
    "password": "123456"
}
```

Response:

```json
{
    "id": 1,
    "name": "Biswajit",
    "email": "biswajit@example.com"
}
```

---

## Login

```http
POST /auth/login
```

Request:

```json
{
    "email": "biswajit@example.com",
    "password": "123456"
}
```

Response:

```json
{
    "access_token": "jwt-token",
    "token_type": "bearer"
}
```

---

# Authorize Swagger

Click:

```text
Authorize
```

Enter:

```text
Bearer <access_token>
```

---

# Protected Endpoints

## Current User

```http
GET /me
```

Returns currently logged-in user.

---

# Task Endpoints

## Create Task

```http
POST /tasks
```

## Get Tasks

```http
GET /tasks
```

## Get Task By ID

```http
GET /tasks/{id}
```

## Update Task

```http
PUT /tasks/{id}
```

## Delete Task

```http
DELETE /tasks/{id}
```

---

# Development

Add New Package:

```bash
uv add package_name
```

Example:

```bash
uv add requests
```

Add Development Dependency:

```bash
uv add --dev pytest
```

Update Environment:

```bash
uv sync
```

---

# Common Commands

Run App:

```bash
uv run uvicorn app.main:app --reload
```

Run Custom Port:

```bash
uv run uvicorn app.main:app --reload --port 9000
```

Install New Package:

```bash
uv add package_name
```

Install Dependencies:

```bash
uv sync
```

Show Installed Packages:

```bash
uv pip list
```

---

# Tech Stack

* FastAPI
* SQLAlchemy
* MySQL
* PyMySQL
* Pydantic
* JWT
* Passlib
* UV
* Uvicorn
