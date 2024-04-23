from utm.core.Domain.DepartmentAdmin import DepartmentAdmin
from .authorised_user import AuthorisedUser


class ProfileViewPolicy:

    @classmethod
    def can_view_all(cls, user: AuthorisedUser):
        return user.user_group in ["Admin"]

    @classmethod
    def can_view_student(
        cls, user: AuthorisedUser, student_email: str, personal_tutor_email: str
    ):
        return (
            user.user_group in ["Admin"]
            or user.user_id == student_email
            or user.user_id == personal_tutor_email
        )

    @classmethod
    def can_view_tutor(cls, user: AuthorisedUser, tutor_email: str):
        return user.user_group in ["Admin"] or user.user_id == tutor_email


class StudentProfileViewPolicy:

    @classmethod
    def is_authorised(cls, user: AuthorisedUser):
        return user.user_group in ["Admin"]


class PersonalTutorPolicy:

    @classmethod
    def can_view_all(cls, user: AuthorisedUser):
        return user.user_group in ["Admin"]

    @classmethod
    def can_view_personal_tutor(cls, user: AuthorisedUser, tutor_email: str):
        return user.user_group in ["Admin"] or user.user_id == tutor_email

    @classmethod
    def can_assign_personal_tutor(cls, user: AuthorisedUser, tutor_department_id: str):
        return (
            user.user_group in ["Admin"] and user.department_id == tutor_department_id
        )

    @classmethod
    def can_update_personal_tutor(
        cls, user: AuthorisedUser, tutor_email: str, tutor_department: str
    ):
        return (
            user.user_group in ["Admin"] or user.user_id == tutor_email
        ) and user.department_id == tutor_department

    @classmethod
    def can_view_schedule(cls, user: AuthorisedUser, tutor_email: str):
        return user.user_group in ["Admin"] or user.user_id == tutor_email


class CohortPolicy:

    @classmethod
    def can_create_cohort(cls, user: AuthorisedUser):
        return user.user_group in ["Admin"]

    @classmethod
    def can_view_all(cls, user: AuthorisedUser):
        return user.user_group in ["Admin"]

    @classmethod
    def can_view_cohort(cls, user: AuthorisedUser, cohort_tutor_email: str):
        return user.user_group in ["Admin"] or cohort_tutor_email == user.user_id

    @classmethod
    def can_assign_tutor_to_cohort(
        cls, user: AuthorisedUser, tutor_department: str, cohort_department: str
    ):
        return (
            user.user_group in ["Admin"]
            and user.department_id == tutor_department == cohort_department
        )

    @classmethod
    def can_add_students_to_cohort(
        cls,
        user: AuthorisedUser,
        cohort_department: str,
        students_department: list[str],
    ):
        return (
            user.user_group in ["Admin"]
            and user.department_id == cohort_department
            and all(
                [department == cohort_department for department in students_department]
            )
        )
