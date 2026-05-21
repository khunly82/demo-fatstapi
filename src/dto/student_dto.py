from dataclasses import dataclass

@dataclass
class StudentDto:
    id: int
    full_name: str
    gender: str