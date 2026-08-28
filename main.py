from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing a to-do list.",
    version="1.0"
)

# Pydantic schema for creating a task
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="The title of the task")

# Pydantic schema for updating a task (fields are optional)
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

# In-memory database
tasks = [
    {"id": 1, "title": "do FlyRank assignment", "done": True},
    {"id": 2, "title": "take Claude subscription", "done": False},
    {"id": 3, "title": "join Micro1 hackerthon", "done": True},
]

@app.get("/")
def root_folder():
    """Returns general metadata about the Task API."""
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    """Health check endpoint to verify the server is active."""
    return {"status": "healthy"}

@app.get("/tasks")
def get_tasks():
    """Retrieve all tasks in the database."""
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Retrieve a single task by its unique ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskCreate):
    """Create a new task with automatic ID assignment."""
    clean_title = task_input.title.strip()
    if not clean_title:
        raise HTTPException(
            status_code=400, detail="Title cannot be empty or blank spaces"
        )
    
    new_task_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    new_task = {
        "id": new_task_id,
        "title": clean_title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_input: TaskUpdate):
    """Update a task's title or completion status by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            if task_input.title is not None:
                clean_title = task_input.title.strip()
                if not clean_title:
                    raise HTTPException(
                        status_code=400, detail="Title cannot be empty or blank spaces"
                    )
                task["title"] = clean_title
            
            if task_input.done is not None:
                task["done"] = task_input.done
                
            return task

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """Delete a task by its ID."""
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")