from typing import Protocol
from ..Common.authorised_user import AuthorisedUser
from ..Common.responses import Result


class IStudentRepository(Protocol):
    def get_students(self, department_id: int): ...

    def get_student_by_id(self, student_id: int): ...

    def get_student_cohorts(self, student_id: int): ...


class IStudentManager(Protocol):

    def request_meeeting(
        self, actor: AuthorisedUser, meeting: dict[str, str]
    ) -> Result: ...

    def get_schedule(
        self, actor: AuthorisedUser, student_id: int, schedule: dict[str, str]
    ) -> Result: ...
