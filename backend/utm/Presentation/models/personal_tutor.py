from datetime import datetime
from pydantic import BaseModel
from typing import List
from .student_cohort import Cohort


class PersonalTutorAssignment(BaseModel):
    department_id: int
    tutor_id: int


class PersonalTutorTrainingStatus(BaseModel):
    id: int
    status: str
    description: str


class PersonalTutor(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    department: str
    training_status: PersonalTutorTrainingStatus
    cohorts: List[Cohort]


class PersonalTutorSchedule(BaseModel):
    start_time: datetime
    end_time: datetime
