from dataclasses import dataclass

@dataclass
class StudentForm:
    last_name: str
    first_name: str
    is_female: bool