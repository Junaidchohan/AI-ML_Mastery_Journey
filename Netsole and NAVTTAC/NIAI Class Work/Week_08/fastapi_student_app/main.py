from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

# Student model
class Student(BaseModel):
    name: str
    age: int
    course: str

@app.get("/")
def home():
    return {"message": "FastAPI Student App Running, message" "FastAPI Student App Running"}

@app.post("/students")
def add_student(student: Student):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }
    students.append(new_student)
    return new_student

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_student(id: int):
    for s in students:
        if s["id"] == id:
            return s
    return {"message": "Student not found"}