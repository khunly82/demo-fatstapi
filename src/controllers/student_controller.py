from fastapi import APIRouter

student_router = APIRouter(prefix="/student")

@student_router.get('')
def get_student():
    return []