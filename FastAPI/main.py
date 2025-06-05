from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class student(BaseModel):
    name: str
    age: int
    grade: str     

students = {
    1: student(name="John", age=20, grade="A"),
    2: student(name="Jack", age=22, grade="B")
}

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/students/{student_id}", response_class=HTMLResponse)
def get_student(request: Request, student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    student_data = students[student_id]
    return templates.TemplateResponse(
        "student.html",
        {"request": request, "student": student_data, "student_id": student_id}
    )