from utm.core.Domain.Student import Student
from utm.core.Domain.PersonalTutor import PersonalTutor
from ..Common.authorised_user import AuthorisedUser
from ..Common.interfaces import IDepartmentRepository, ISchoolLmsRepository
from ..Common.responses import Result, SuccessResult, FailureResult, ResponseTypes
from ..Common._exceptions import UTMApplicationError
from ..Common.policies import CohortPolicy
from .interfaces import ICohortManager
from datetime import datetime
from utm.core.Domain.Cohort import Cohort


class CohortManager(ICohortManager):

    def __init__(
        self, repository: IDepartmentRepository, school_lms: ISchoolLmsRepository
    ):
        self.repository = repository
        self.school_lms = school_lms

    def create_cohort(self, user: AuthorisedUser, cohort_data: dict) -> Result:
        if not CohortPolicy.can_create_cohort(user):
            return FailureResult(
                ResponseTypes.PERMISSION_ERROR,
                "You do not have permission to perform this action",
            )

        try:
            cohort = Cohort.create(user.department_id, cohort_data)
            cohort.academic_session.set_session_data(
                self.school_lms.get_academic_session(cohort.academic_session.id)
            )
            new_cohort = Cohort(
                **self.repository.add_cohort(cohort.serialise(with_tutors=True))
            )
        except UTMApplicationError as exc:
            return FailureResult(ResponseTypes.RESOURCE_ERROR, exc)
        return SuccessResult(_value=new_cohort.serialise())

    def get_cohorts(self, user: AuthorisedUser) -> Result:
        if not CohortPolicy.can_view_all(user):
            return FailureResult(
                ResponseTypes.PERMISSION_ERROR,
                "You do not have permission to perform this action",
            )

        try:
            cohorts = [
                Cohort(**cohort)
                for cohort in self.repository.get_cohorts(user.department_id)
            ]
            academic_sessions = self.school_lms.get_academic_sessions_by_ids(
                [cohort.academic_session.id for cohort in cohorts]
            )
            for cohort in cohorts:
                cohort.academic_session.set_session_data(
                    academic_sessions[cohort.academic_session.id]
                )
        except UTMApplicationError as exc:
            return FailureResult(ResponseTypes.RESOURCE_ERROR, exc)

        return SuccessResult([cohort.serialise() for cohort in cohorts])

    def get_cohort(self, user: AuthorisedUser, cohort_id: int) -> Result:

        try:
            cohort = Cohort(**self.repository.get_cohort(cohort_id))
            if not CohortPolicy.can_view_cohort(user, cohort.personal_tutor.email):
                return FailureResult(
                    ResponseTypes.PERMISSION_ERROR,
                    "You do not have permission to perform this action",
                )
            academic_session = self.school_lms.get_academic_session(
                cohort.academic_session.id
            )
            cohort.academic_session.set_session_data(academic_session)
        except UTMApplicationError as exc:
            return FailureResult(ResponseTypes.RESOURCE_ERROR, exc)
        return SuccessResult(cohort.serialise())

    def assign_personal_tutor_to_cohort(
        self, user: AuthorisedUser, cohort_id: int, personal_tutor_id: int
    ) -> Result:

        try:
            cohort = Cohort(**self.repository.get_cohort(cohort_id))
            cohort.academic_session.set_session_data(
                self.school_lms.get_academic_session(cohort.academic_session.id)
            )

            personal_tutor = PersonalTutor(
                **self.repository.get_personal_tutor_by_id(personal_tutor_id)
            )
            cohort.new_personal_tutor(personal_tutor)
            if not CohortPolicy.can_assign_tutor_to_cohort(
                user, cohort.department, personal_tutor.department
            ):
                return FailureResult(
                    ResponseTypes.PERMISSION_ERROR,
                    "You do not have permission to perform this action",
                )
            updated_cohort = Cohort(
                **self.repository.set_cohort_tutor(
                    _id=cohort.id,
                    department=cohort.department,
                    cohort_tutor_data=cohort.personal_tutor.serialise(
                        include_active=True
                    ),
                )
            )
        except UTMApplicationError as exc:
            return FailureResult(ResponseTypes.RESOURCE_ERROR, exc)

        print("Updated Cohort: ", updated_cohort.serialise())
        return SuccessResult(updated_cohort.serialise())

    def add_students_to_cohort(
        self, user: AuthorisedUser, cohort_id: int, students: list[str]
    ) -> Result:
        try:
            cohort = Cohort(**self.repository.get_cohort(cohort_id))
            cohort.academic_session.set_session_data(
                self.school_lms.get_academic_session(cohort.academic_session.id)
            )
            student_data = [
                Student(**self.repository.get_student_by_id(student_id))
                for student_id in students
            ]
            if not CohortPolicy.can_add_students_to_cohort(
                user,
                cohort.department,
                [student.department for student in student_data],
            ):
                return FailureResult(
                    ResponseTypes.PERMISSION_ERROR,
                    "You do not have permission to perform this action",
                )
            student_data = [student.to_student_base() for student in student_data]
            cohort.update_students(student_data)
            updated_cohort = Cohort(
                **self.repository.add_students_to_cohort(
                    _id=cohort.id,
                    department=cohort.department,
                    cohort_students_data=[
                        student.serialise() for student in cohort.students
                    ],
                )
            )
        except UTMApplicationError as exc:
            return FailureResult(ResponseTypes.RESOURCE_ERROR, exc)

        return SuccessResult(updated_cohort.serialise())
