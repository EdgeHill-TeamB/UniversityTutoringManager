from pydantic import BaseModel
from .StudentBase import StudentBase
from .CohortBase import CohortBase
from typing import List


class AcademicSession(BaseModel):
    id: str
    name: str
    start_date: str
    end_date: str


class CohortStudentProfile(StudentBase):
    def __post_init__(self):
        self.id = str(self.id)


class StudentProfile(StudentBase):
    department: str
    cohort: CohortBase
    academic_session: AcademicSession

    @property
    def has_cohort(self) -> bool:
        return self.cohort is not None


class AddStudentsToCohort(BaseModel):
    student_ids: List[str]
