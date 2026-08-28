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

GET /healthLiveness check endpoint for load balancers and service orchestration.  Response (200 OK):JSON{
  "status": "healthy"
}
2. Task Resource Management (/tasks)GET /tasksRetrieves the complete list of tasks.  Response (200 OK):JSON[
  {"id": 1, "title": "do FlyRank assignment", "done": true},
  {"id": 2, "title": "take Claude subscription", "done": false},
  {"id": 3, "title": "join Micro1 hackerthon", "done": true}
]
GET /tasks/{task_id}Retrieves a single task by its unique integer path parameter.  Response (200 OK):JSON{"id": 2, "title": "take Claude subscription", "done": false}
Error Response (404 Not Found):JSON{"detail": "Task 99 not found"}
POST /tasksCreates a new task[cite: 1]. Automatically computes incremental ID assignment and defaults done status to false[cite: 1].Request Body:JSON{
  "title": "Build production API"
}
Response (201 Created):JSON{
  "id": 4,
  "title": "Build production API",
  "done": false
}
Validation Error (400 Bad Request - Blank/Whitespace Title):JSON{"detail": "Title cannot be empty or blank spaces"}
PUT /tasks/{task_id}Updates an existing task[cite: 1]. Accepts partial updates for title or done fields via optional payload definitions[cite: 1].Request Body (Updating status):JSON{
  "done": true
}
Response (200 OK):JSON{
  "id": 2,
  "title": "take Claude subscription",
  "done": true
}
Error Response (404 Not Found):JSON{"detail": "Task 99 not found"}
DELETE /tasks/{task_id}Removes a task from the state store by ID[cite: 1].Response (204 No Content): Empty payload body[cite: 1]Error Response (404 Not Found):JSON{"detail": "Task 99 not found"}
