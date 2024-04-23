from ..Common.interfaces import IDepartmentRepository, ISchoolLmsRepository
from ..Common.policies import ProfileViewPolicy
from ..Common.responses import SuccessResult, FailureResult, ResponseTypes, Result
from ..Common._exceptions import UTMApplicationError
from ..Common.authorised_user import AuthorisedUser
from utm.core.Domain.DepartmentAdmin import DepartmentAdmin
from utm.core.Domain.Tutor import Tutor
from utm.core.Domain.Student import Student


class DepartmentManager:
    def __init__(
        self, repository: IDepartmentRepository, school_lms: ISchoolLmsRepository
    ):
        self.repository = repository
        self.school_lms = school_lms

    def get_staff(self, user: AuthorisedUser) -> Result:
        if not ProfileViewPolicy.can_view_all(user):
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

    def get_students(self, user: AuthorisedUser, filters: dict[str] = None) -> Result:
        if not ProfileViewPolicy.can_view_all(user):
            return FailureResult(
                message="You do not have permission to view this resource",
                type_=ResponseTypes.PERMISSION_ERROR,
            )
        try:
            students_data = self.repository.get_students_by_department_id(
                user.department_id, filters
            )

            students = [Student(**student) for student in students_data]
            academic_sessions = self.school_lms.get_academic_sessions_by_ids(
                [student.academic_session.id for student in students]
            )
            for student in students:
                student.academic_session.set_session_data(
                    academic_sessions[student.academic_session.id]
                )

            result = [student.serialise() for student in students]

        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

        return SuccessResult(result)

    def get_student_by_id(self, user: AuthorisedUser, student_id) -> Result:
        try:
            # get student details
            student_data = self.repository.get_student_by_id(student_id)

            # get personal tutor email
            personal_tutor = self.repository.get_personal_tutor_by_student_id(
                student_id
            )
            personal_tutor_email = (
                personal_tutor.get("email", "") if personal_tutor else ""
            )

            # check if user has permission to view student details
            if not ProfileViewPolicy.can_view_student(
                user, student_data["email"], personal_tutor_email
            ):
                return FailureResult(
                    message="You do not have permission to view this resource",
                    type_=ResponseTypes.PERMISSION_ERROR,
                )
            student = Student(**student_data)
            academic_session = self.school_lms.get_academic_session(
                student.academic_session.id
            )
            student.academic_session.set_session_data(academic_session)
            result = student.serialise()

        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

        return SuccessResult(result)

    def get_tutors(self, user: AuthorisedUser) -> Result:
        if not ProfileViewPolicy.can_view_all(user):
            return FailureResult(
                message="You do not have permission to view this resource",
                type_=ResponseTypes.PERMISSION_ERROR,
            )
        try:
            tutors = self.repository.get_tutors_by_department_id(user.department_id)
            return SuccessResult([Tutor(**tutor).serialise() for tutor in tutors])
        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

    def get_tutor_by_id(self, user: AuthorisedUser, tutor_id: str) -> Result:
        try:
            tutor = self.repository.get_tutor_by_id(tutor_id)

            if not ProfileViewPolicy.can_view_tutor(user, tutor["email"]):
                return FailureResult(
                    message="You do not have permission to view this resource",
                    type_=ResponseTypes.PERMISSION_ERROR,
                )

        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

        return SuccessResult(Tutor(**tutor).serialise())
