from .CohortBase import CohortBase
from .StudentBase import StudentBase
from .PersonalTutorBase import PersonalTutorBase, PersonalTutorTraining
from typing import List, Optional
from pydantic import BaseModel


class CohortPersonalTutor(PersonalTutorBase):
    training: PersonalTutorTraining
    start_date: str
    end_date: str


class CohortProfile(CohortBase):
    department: str
    academic_session: dict[str, str]
    students: List[StudentBase] = []
    personal_tutor: Optional[CohortPersonalTutor] = None


class CohortCreate(BaseModel):
    name: str
    academic_session: str
