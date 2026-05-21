from .db import Base
from sqlalchemy.orm import Mapped, mapped_column

class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    last_name: Mapped[str] = mapped_column() 
    first_name: Mapped[str] = mapped_column()
    is_female: Mapped[bool] = mapped_column(default=True)
     