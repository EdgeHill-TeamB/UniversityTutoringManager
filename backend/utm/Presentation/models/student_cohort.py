from __future__ import annotations
from pydantic import BaseModel
from typing import List

# from .personal_tutor import PersonalTutor


class Cohort(BaseModel):
    id: int
    name: str
    department: str
    start_date: int
    end_date: int
    students: int
    # personal_tutor_assignment: List[PersonalTutor]
