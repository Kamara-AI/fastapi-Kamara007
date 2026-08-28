 #import FastAPI class from fastapi module
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Create an instance of the FastAPI application.
app = FastAPI()

# Pydantic schema for creating a task
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="The title of the task")

# Pydantic schema for updating a task (optional fields)
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

# In-memory database
tasks = [
    {"id": 1, "title": "do FlyRank assignment", "done": True},
    {"id": 2, "title": "take Claude subscription", "done": False},
    {"id": 3, "title": "join Micro1 hackerthon", "done": True},
]

# GET ENDPOINTS
@app.get("/")
def root_folder():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


# POST ENDPOIN
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskCreate):
    clean_title = task_input.title.strip()
    if not clean_title:
        
        raise HTTPException(
            status_code=400, detail="Title cannot be empty or blank spaces"
        )
    
    # Generate a new task ID
    new_task_id = max(task["id"] for task in tasks) + 1 if tasks else 1

    # Create a new task dictionary
    new_task = {
        "id": new_task_id,
        "title": clean_title,
        "done": False
    }

    # Add the new task to the in-memory database
    tasks.append(new_task)

    return new_task


#  PUT ENDPOINT
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_input: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
        # Update title if provided
            if task_input.title is not None:
                clean_title = task_input.title.strip()
                if not clean_title:
                    raise HTTPException(
                        status_code=400, detail="Title cannot be empty or blank spaces"
                    )
                task["title"] = clean_title
            
            # Update completion status if provided
            if task_input.done is not None:
                task["done"] = task_input.done
                
            return task

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

# DELETE ENDPOINT
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            # 204 No Content responses do not return a body payload
            return

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")