from typing import Protocol
from ..Common.responses import Result
from ..Common.authorised_user import AuthorisedUser


class IDepartmentManager(Protocol):

    def get_staff(user: AuthorisedUser) -> Result: ...

    def get_students(user: AuthorisedUser, filters: dict[str, str]) -> Result: ...

    def get_student_by_id(user: AuthorisedUser, student_id: int) -> Result: ...

    def get_tutors(user: AuthorisedUser, department_id: int) -> Result: ...

    def get_tutor_by_id(tutor_id: int, user: AuthorisedUser) -> Result: ...

    def assign_tutor_as_personal_tutor(
        user: AuthorisedUser, tutor_id: int
    ) -> Result: ...
