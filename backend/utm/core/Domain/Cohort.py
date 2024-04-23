from datetime import datetime
from .StudentBase import StudentBase
from .PersonalTutor import CohortPersonalTutor, PersonalTutor
from .CohortBase import CohortBase


class Cohort(CohortBase):
    def __init__(
        self,
        name: str,
        department: str,
        start_date: str,
        academic_session: str,
        students: list[dict[str, str]] = [],
        tutors: list[dict[str, str]] = [],
        id: str = None,
    ):
        super().__init__(name, start_date, academic_session, id)
        self.department = department
        self.students = [StudentBase(**student) for student in students]
        self.tutors = [CohortPersonalTutor(**tutor) for tutor in tutors]

    def new_personal_tutor(self, personal_tutor: PersonalTutor):
        for tutor in self.tutors:
            if tutor.is_active:
                tutor.is_active = False
                tutor.end_date = datetime.now().strftime("%Y-%m-%d")
        cohort_personal_tutor = CohortPersonalTutor.from_personal_tutor(personal_tutor)
        cohort_personal_tutor.is_active = True
        cohort_personal_tutor.start_date = datetime.now().strftime("%Y-%m-%d")
        cohort_personal_tutor.end_date = ""
        self.tutors.append(cohort_personal_tutor)

    def update_students(self, students: list[StudentBase]):
        self.students.extend(students)

    @property
    def personal_tutor(self) -> CohortPersonalTutor:
        for tutor in self.tutors:
            if tutor.is_active:
                return tutor
        return None

    @classmethod
    def create(cls, department, cohort_data: dict[str, str]):
        return cls(
            name=cohort_data["name"],
            department=department,
            start_date=datetime.now().strftime("%Y-%m-%d"),
            academic_session={"id": cohort_data["academic_session"]},
        )

    def notify(self, message): ...

    def serialise(self, with_tutors=False):
        result = {
            **super().serialise(),
            "department": self.department,
            "students": [student.serialise() for student in self.students],
        }
        if not with_tutors:
            result["personal_tutor"] = (
                self.personal_tutor.serialise() if self.personal_tutor else None
            )
        else:
            result["tutors"] = [tutor.serialise() for tutor in self.tutors]
        return result
