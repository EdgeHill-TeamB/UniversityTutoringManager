from .StudentBase import StudentBase
from .AcademicSession import AcademicSession


class Student(StudentBase):

    def __init__(
        self,
        id: str,
        first_name: str = None,
        last_name: str = None,
        email: str = None,
        department: str = None,
        academic_session: dict[str, str] = None,
        module: str = None,
        cohort: dict[str, str] = None,
    ):
        super().__init__(id, first_name, last_name, email, module)
        self.department = department
        self.academic_session = AcademicSession(**academic_session)
        self.cohort = cohort

    def to_student_base(self) -> StudentBase:
        return StudentBase(
            self.id, self.first_name, self.last_name, self.email, self.module
        )

    def get_attendance_record(self):
        pass

    def notify(self, message):
        pass

    def serialise(self) -> dict[str, str]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "module": self.module,
            "department": self.department,
            "academic_session": self.academic_session.serialise(),
            "cohort": self.cohort,
        }
