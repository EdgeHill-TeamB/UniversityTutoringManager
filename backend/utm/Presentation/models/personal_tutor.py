from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from typing import List
from .PersonalTutorBase import PersonalTutorBase, PersonalTutorTraining


class PersonalTutorUpdate(BaseModel):
    email: str = None
    training: PersonalTutorTraining = None

    def __post_init__(self):
        if self.training is None and self.email is None:
            raise ValueError("At least one of email or training field must be provided")


class PersonalTutor(PersonalTutorBase):
    department: str
    training: PersonalTutorTraining


class PersonalTutorSchedule(BaseModel):
    start_time: datetime
    end_time: datetime
