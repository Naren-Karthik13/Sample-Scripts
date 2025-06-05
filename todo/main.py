from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class task(BaseModel):
    task_id: int
    title: str
    description: str
    completed: bool

tasks = []
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: task):
    tasks.append(task)
    return {"message": "Task created successfully", "task": task}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.task_id == task_id:
            return task
    return {"message": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: task):
    for index, task in enumerate(tasks):
        if task.task_id == task_id:
            tasks[index] = updated_task
            return {"message": "Task updated successfully", "task": updated_task}
    return {"message": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.task_id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}

