from fastapi import APIRouter, Request, Depends
from sqlalchemy import select
from src.dto.student_dto import StudentDto
from src.dto.student_form import StudentForm
from src.models import Session, Student
from sqlalchemy.orm import Session as SqlSession 

student_router = APIRouter(prefix="/student")

@student_router.get('')
def get_student(
    _: Request, 
    session: SqlSession = Depends(Session)
) -> list[StudentDto]:
    stmt = select(Student)
    students = session.scalars(stmt).all()
    return [StudentDto(
        id=item.id,
        full_name=f'{item.last_name} {item.first_name}',
        gender='Female' if item.is_female else 'Male'
    ) for item in students]

@student_router.post('')
def add_student(
    _: Request, 
    form: StudentForm, 
    session: SqlSession = Depends(Session)
) -> Student:
    student = Student(**form.__dict__)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student