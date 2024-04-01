from pydantic import BaseModel
from ..models.cohort import Cohort


class Staff(BaseModel):
    id: int
    name: str
    email: str
    office_no: str
    dept_id: int
    role: list[str]
    training_status: bool
    cohort_id: Cohort.id


class StaffFilter(BaseModel):
    id: int
    dept_id: int
    cohort_id: Cohort.id
