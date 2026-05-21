from fastapi import APIRouter, Request, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from src.dto.student_dto import StudentDto
from src.dto.student_form import StudentForm
from src.models.db import get_session
from src.models.student import Student

student_router = APIRouter(prefix="/student")

template = Jinja2Templates(directory='src/views')

@student_router.get('')
def get_student(
    request: Request, 
    session: Session = Depends(get_session)
):
    stmt = select(Student)
    students = session.scalars(stmt).all()
    view_model = [StudentDto(
        id=item.id,
        full_name=f'{item.last_name} {item.first_name}',
        gender='Female' if item.is_female else 'Male'
    ) for item in students]
    return template.TemplateResponse(
        name='student/index.html', 
        request=request,
        context={
            'students': view_model
        }
    )

@student_router.post('')
def add_student(
    _: Request, 
    form: StudentForm, 
    session: Session = Depends(get_session)
) -> Student:
    student = Student(**form.__dict__)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student