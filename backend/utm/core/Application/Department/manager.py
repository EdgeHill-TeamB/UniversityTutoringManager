from .Interfaces import IDepartmentRepository
from .policies import ProfileViewPolicy
from ..Common.responses import SuccessResult, FailureResult, ResponseTypes, Result
from ..Common._exceptions import UTMApplicationError
from ..Common.authorised_user import AuthorisedUser
from utm.core.Domain.DepartmentAdmin import DepartmentAdmin
from utm.core.Domain.Tutor import Tutor
from utm.core.Domain.Student import Student


class DepartmentManager:
    def __init__(self, repository: IDepartmentRepository):
        self.repository = repository

    def get_staff(self, user: AuthorisedUser) -> Result:
        if not ProfileViewPolicy.can_view_members(user):
            return FailureResult(
                message="You do not have permission to view this resource",
                type_=ResponseTypes.PERMISSION_ERROR,
            )
        try:
            administrators = self.repository.get_admin_by_department_id(
                user.department_id
            )
            tutors = self.repository.get_tutors_by_department_id(user.department_id)

            return SuccessResult(
                {
                    "admin": [
                        DepartmentAdmin(**admin).serialise() for admin in administrators
                    ],
                    "tutors": [Tutor(**tutor).serialise() for tutor in tutors],
                }
            )
        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

    def get_students(self, user, department_id) -> Result:
        if not ProfileViewPolicy.can_view_members(user, department_id):
            return FailureResult(
                message="You do not have permission to view this resource",
                type_=ResponseTypes.PERMISSION_ERROR,
            )
        try:
            students = self.repository.get_students_by_department_id(department_id)
            return SuccessResult(
                {
                    "students": [
                        Student(**student).serialise() for student in students
                    ],
                }
            )
        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

    def get_student_by_id(self, user, student_id) -> Result: ...

    def get_tutors(self, user, department_id, status) -> Result: ...

    def get_tutor_by_id(self, tutor_id, user) -> Result: ...

    def assign_tutor_as_personal_tutor(self, user, tutor_id) -> Result: ...
