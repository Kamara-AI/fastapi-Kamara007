# Task API

A production-grade, asynchronous RESTful API built with Python and FastAPI for managing a task lifecycle. Features strict type enforcement via Pydantic v2 schemas, precise HTTP status codes, structured JSON error responses, and automated interactive OpenAPI documentation.

---

## Technical Stack & Features

* **Framework:** FastAPI (Python 3.10+)
* **Validation & Schemas:** Pydantic v2
* **Documentation:** OpenAPI 3.1 & Swagger UI (`/docs`)
* **Architecture:** Asynchronous REST endpoints with strict HTTP status code adherence (200, 201, 204, 400, 404, 422)
* **Data Storage:** In-memory state storage

---

## Endpoint Summary Table

| Method | Endpoint | Description | Expected Status Codes |
|---|---|---|---|
| GET | `/` | API metadata | 200 OK |
| GET | `/health` | Health check endpoint | 200 OK |
| GET | `/tasks` | List all tasks | 200 OK |
| GET | `/tasks/{id}` | Retrieve specific task by ID | 200 OK / 404 Not Found |
| POST | `/tasks` | Create new task | 201 Created / 400 Bad Request |
| PUT | `/tasks/{id}` | Update title or completion status | 200 OK / 400 / 404 |
| DELETE | `/tasks/{id}` | Delete task by ID | 204 No Content / 404 Not Found |

---

## API Architecture & Detailed Endpoint Specifications

### 1. Root & Diagnostics

#### `GET /`
Returns general service metadata.
* **Response (200 OK):**
  ```json
  {
    "name": "Task API",
    "version": "1.0",
    "endpoints": ["/tasks"]
  }
