from typing import Protocol
from ..Common.responses import Result
from ..Common.authorised_user import AuthorisedUser
from ..Common._exceptions import UTMApplicationError
from enum import Enum


class TutorEnum(str, Enum):
    all = "all"
    assigned = "assigned"
    unassigned = "unassigned"


class IDepartmentRepository(Protocol):

    def set_resource_exception(exc: UTMApplicationError): ...

    def get_admin_by_department_id(department_id: str): ...

    def get_tutors_by_department_id(department_id: str): ...

    def get_students_by_department_id(department_id: str): ...


class IDepartmentManager(Protocol):

    def get_staff(user: AuthorisedUser) -> Result: ...

    def get_students(user: AuthorisedUser, department_id: int) -> Result: ...

    def get_student_by_id(user: AuthorisedUser, student_id: int) -> Result: ...

    def get_tutors(
        user: AuthorisedUser, department_id: int, status: TutorEnum
    ) -> Result: ...

    def get_tutor_by_id(tutor_id: int, user: AuthorisedUser) -> Result: ...

    def assign_tutor_as_personal_tutor(
        user: AuthorisedUser, tutor_id: int
    ) -> Result: ...
