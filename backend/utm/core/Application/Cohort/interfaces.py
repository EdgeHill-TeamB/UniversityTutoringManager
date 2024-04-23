from typing import Protocol

from ..Common.authorised_user import AuthorisedUser
from ..Common.responses import Result


class ICohortManager(Protocol):

    def create_cohort(
        self, actor: AuthorisedUser, cohort_data: dict[str, str]
    ) -> Result: ...

    def get_cohorts(self, actor: AuthorisedUser) -> Result: ...

    def get_cohort(self, actor: AuthorisedUser, cohort_id: int) -> Result: ...

    def add_students_to_cohort(
        self, user: AuthorisedUser, cohort_id: int, students: list[dict[str, str]]
    ) -> Result: ...

    def assign_personal_tutor_to_cohort(
        self, user: AuthorisedUser, cohort_id: int, personal_tutor_id: int
    ) -> Result: ...

    def get_cohort_students(self, actor: AuthorisedUser, cohort_id: int) -> Result: ...

    def notify(self, actor: AuthorisedUser, cohort_id: int, message: str) -> Result: ...
