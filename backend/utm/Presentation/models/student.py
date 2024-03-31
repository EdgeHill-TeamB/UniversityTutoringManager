from pydantic import BaseModel
from . import staff

class Student(BaseModel):
    id: int
    name: str
    email: str
    dept_id: int
    tutor_id: staff.Staff.id



class studentFilter(BaseModel):
    id: int
    dept_id: int
    tutor_id: staff.Staff.id
