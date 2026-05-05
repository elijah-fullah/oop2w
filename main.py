#Importing FastAPI Library
from fastapi import FastAPI

#Creating the App
app = FastAPI()

#Get Method
@app.get("/students/{student_id}")

#Function
async def get_all_students(student_id: int):
    students = {
        1: {'name': 'Salome', 'grade': 'A'},
    }

    if student_id in students:
        return {"student_id": student_id, **students[student_id]}
    else:
        return {'Error': f'Student with id {student_id} not found!'}