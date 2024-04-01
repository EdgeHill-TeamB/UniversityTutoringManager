from pydantic import BaseModel
from . import staff
from ..models.cohort import Cohort

class Student(BaseModel):
    id: int
    name: str
    email: str
    dept_id: int
    cohort_id: Cohort.id



class studentFilter(BaseModel):
    id: int
    dept_id: int
    cohort_id: Cohort.id
