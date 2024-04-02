from typing import Protocol

from ..Common.authorised_user import AuthorisedUser
from ..Common.responses import Result


class ICohortRepository(Protocol):

    def get_cohorts(self, department_id: int): ...

    def get_cohort_by_id(self, cohort_id: int): ...

    def get_cohort_students(self, cohort_id: int): ...

    def get_cohort_personal_tutors(self, cohort_id: int): ...


class ICohortManager(Protocol):

    def create_cohort(
        self, actor: AuthorisedUser, cohort: dict[str, str]
    ) -> Result: ...

    def assign_students_to_cohort(
        self, actor: AuthorisedUser, cohort_id: int, student_list: list[dict[str, str]]
    ) -> Result: ...

    def assign_personal_tutor_to_cohort(
        self, actor: AuthorisedUser, cohort_id: int, tutor_id: int
    ) -> Result: ...

    def get_cohort_students(self, actor: AuthorisedUser, cohort_id: int) -> Result: ...

    def notify(self, actor: AuthorisedUser, cohort_id: int, message: str) -> Result: ...
