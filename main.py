#Importing my FASTAPI library
from fastapi import FastAPI

#Create app
app = FastAPI()

#Get Method
@app.get("/students/{student_id}")

#Function
async def home(student_id: int):
    #Return Message
    student = {
        1: {"name": "fatu", 'grade': 'a'},

    }
    if student_id in student:
        return {"student_id": student_id, **student[student_id]}
    else:
        return {"Error": f"Student with id {student_id} does not exist"}