 #import FastAPI class from fastapi module
from fastapi import FastAPI, HTTPException


# Create an instance of the FastAPI application.
# This 'app' object acts as the central server that handles incoming requests.
app = FastAPI()

# In-memory database
tasks = [
    {"id": 1, "title":"do FlyRank assignment", "done": True},
    {"id": 2, "title":"take Claude subscription", "done": False},
    {"id": 3, "title":"join Micro1 hackerthon", "done": True},

 ]

#Tell FASTAPI to listen for incoming requests on GET root URL ("/")
@app.get("/")
def root_folder ():
    return {"name": "Task API",
    "version":"1.0",
    "endpoint":["/tasks"]
    }

@app.get("/health")
def health ():
    return {"status":"healthy"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail= f"Task {task_id} not found")
