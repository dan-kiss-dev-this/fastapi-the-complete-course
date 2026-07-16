# FastAPI - The Complete Course

Dan working through a course created by Eric Roby. This repository contains progressively more complex FastAPI projects built throughout the course, plus a Python refresher section.

---

## Project Structure

| Folder | Description |
|---|---|
| `PythonRefresher/` | Python fundamentals (variables, loops, OOP, etc.) |
| `Project 1/` | Basic Books API — path params, query params, CRUD |
| `Project 2/` | Books API v2 — Pydantic models and request validation |
| `Project 3/` | TodoApp — SQLite, SQLAlchemy ORM, JWT authentication |
| `Project 3.5/` | TodoApp — adds Alembic database migrations |
| `Project 4/` | TodoApp — adds automated testing with pytest |
| `Project 5/` | TodoApp — adds Jinja2 templates and static files |

---

## Prerequisites

- Python 3.11+
- pip

---

## Setup

**1. Clone the repository**
```bash
git clone <repo-url>
cd fastapi-the-complete-course
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Running the Applications

### Project 1 — Books API

```bash
cd "Project 1"
uvicorn books:app --reload
```

### Project 2 — Books API v2

```bash
cd "Project 2"
uvicorn books2:app --reload
```

### Project 3 — TodoApp (SQLite + Auth)

```bash
cd "Project 3/TodoApp"
uvicorn main:app --reload
```

### Project 3.5 — TodoApp with Alembic

```bash
cd "Project 3.5/TodoApp"
uvicorn main:app --reload
```

### Project 4 — TodoApp with Tests

```bash
cd "Project 4/TodoApp"
uvicorn main:app --reload
```

Run tests:
```bash
pytest
```

### Project 5 — TodoApp with Templates

```bash
cd "Project 5/TodoApp"
uvicorn main:app --reload
```

---

## Accessing the API

Once running, open your browser to:

- **Interactive docs (Swagger UI):** http://127.0.0.1:8000/docs
- **Alternative docs (ReDoc):** http://127.0.0.1:8000/redoc
- **App root:** http://127.0.0.1:8000

---

## TodoApp API Endpoints (Project 3+)

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Get all todos |
| GET | `/todo/{id}` | Get a single todo by ID |
| POST | `/todo` | Create a new todo |
| PUT | `/todo/{id}` | Update an existing todo |
| DELETE | `/todo/{id}` | Delete a todo |
| POST | `/auth/` | Register a new user |
| POST | `/auth/token` | Login and get JWT token |

---

## Debugging in PyCharm

Each `main.py` includes an entry point for PyCharm's debugger:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

Right-click `main.py` in PyCharm and select **Debug** to launch with breakpoints enabled.

---

## Database

Project 3 uses SQLite. The database file `todos.db` is created automatically on first run in `Project 3/TodoApp/`.

To inspect it in PyCharm:
1. **View → Tool Windows → Database**
2. Click **+** → **Data Source** → **SQLite**
3. Browse to `Project 3/TodoApp/todos.db`
4. Click **Test Connection**, then **OK**
