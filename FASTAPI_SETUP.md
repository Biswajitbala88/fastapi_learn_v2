# FastAPI Project Setup Guide (Modern UV Workflow)

## 1. Create Project Folder

```powershell
mkdir my_fastapi_project
cd my_fastapi_project
```

---

## 2. Install UV

```powershell
pip install uv
```

Verify:

```powershell
uv --version
```

---

## 3. Initialize Project

```powershell
uv init
```

Generated files:

```text
my_fastapi_project/
├── .python-version
├── pyproject.toml
├── README.md
└── src/
```

`pyproject.toml` is the Python equivalent of `package.json`.

---

## 4. Add Dependencies

Install FastAPI and Uvicorn:

```powershell
uv add fastapi uvicorn
```

Install SQLAlchemy:

```powershell
uv add sqlalchemy
```

Install Pydantic:

```powershell
uv add pydantic
```

Install MySQL Driver:

```powershell
uv add pymysql
```

Install PostgreSQL Driver:

```powershell
uv add psycopg2-binary
```

---

## 5. Project Structure

```text
my_fastapi_project/
│
├── pyproject.toml
├── uv.lock
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   └── task.py
│   │
│   ├── schemas/
│   │   └── task_schema.py
│   │
│   ├── routers/
│   │   └── task_router.py
│   │
│   └── services/
│
└── tests/
```

---

## 6. Create main.py

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

---

## 7. Run Application

```powershell
uv run uvicorn app.main:app --reload
```

Custom Port:

```powershell
uv run uvicorn app.main:app --reload --port 9000
```

Custom Host + Port:

```powershell
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 9000
```

---

## 8. API Documentation

Swagger UI:

```text
http://127.0.0.1:9000/docs
```

ReDoc:

```text
http://127.0.0.1:9000/redoc
```

---

## 9. Add New Package

Equivalent to:

```bash
npm install package-name
```

Use:

```powershell
uv add package-name
```

Example:

```powershell
uv add requests
```

---

## 10. Development Dependencies

Equivalent to:

```bash
npm install --save-dev pytest
```

Use:

```powershell
uv add --dev pytest
```

Example:

```powershell
uv add --dev black
uv add --dev pytest
uv add --dev ruff
```

---

## 11. Install Dependencies on Another Machine

Equivalent to:

```bash
npm install
```

Use:

```powershell
uv sync
```

This installs everything from:

```text
pyproject.toml
uv.lock
```

---

## 12. Node.js vs Python

```text
Node.js                     Python

package.json       →        pyproject.toml
package-lock.json  →        uv.lock
npm install        →        uv sync
npm install pkg    →        uv add pkg
npm run            →        uv run
express            →        FastAPI
node server.js     →        uvicorn main:app
```

---

## 13. Typical Workflow

```powershell
mkdir my_fastapi_project
cd my_fastapi_project

uv init

uv add fastapi uvicorn sqlalchemy pydantic

uv run uvicorn app.main:app --reload --port 9000
```

Open:

```text
http://127.0.0.1:9000/docs
```

This is the modern FastAPI workflow and closely matches the Node.js package.json experience.
