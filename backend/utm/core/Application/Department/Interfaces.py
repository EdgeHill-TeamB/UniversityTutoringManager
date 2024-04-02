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

    def get_staff(self, actor: AuthorisedUser, department_id: int) -> Result: ...

    def get_students(self, actor: AuthorisedUser, department_id: int) -> Result: ...

    def get_student_by_id(self, actor: AuthorisedUser, student_id: int) -> Result: ...

    def get_tutors(
        self, actor: AuthorisedUser, department_id: int, status: TutorEnum
    ) -> Result: ...

    def get_tutor_by_id(self, tutor_id: int, actor: AuthorisedUser) -> Result: ...

    def assign_tutor_as_personal_tutor(
        self, actor: AuthorisedUser, tutor_id: int
    ) -> Result: ...
