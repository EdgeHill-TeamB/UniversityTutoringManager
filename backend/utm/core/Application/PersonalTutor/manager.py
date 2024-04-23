from .interfaces import IPersonalTutorManager
from ..Common.authorised_user import AuthorisedUser
from ..Common.responses import Result, SuccessResult, FailureResult, ResponseTypes
from ..Common._exceptions import UTMApplicationError
from ..Common.interfaces import IDepartmentRepository
from ..Common.policies import PersonalTutorPolicy
from utm.core.Domain.PersonalTutor import PersonalTutor, Training
from datetime import datetime


class PersonalTutorManager(IPersonalTutorManager):
    def __init__(self, repository: IDepartmentRepository) -> None:
        self.repository = repository

    def get_personal_tutors(self, user: AuthorisedUser) -> Result:
        if not PersonalTutorPolicy.can_view_all(user):
            return FailureResult(
                message="You do not have permission to view this resource",
                type_=ResponseTypes.PERMISSION_ERROR,
            )
        try:
            personal_tutors = self.repository.get_personal_tutors_by_department_id(
                user.department_id
            )
            result = [PersonalTutor(**tutor).serialise() for tutor in personal_tutors]

        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )
        return SuccessResult(result)

    def get_personal_tutor(self, user: AuthorisedUser, tutor_id: int) -> Result:

        try:
            tutor = self.repository.get_personal_tutor_by_id(tutor_id)
            if not PersonalTutorPolicy.can_view_personal_tutor(user, tutor["email"]):
                return FailureResult(
                    message="You do not have permission to view this resource",
                    type_=ResponseTypes.PERMISSION_ERROR,
                )
            return SuccessResult(PersonalTutor(**tutor).serialise())
        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

    def assign_tutor_as_personal_tutor(
        self, user: AuthorisedUser, tutor_id: int
    ) -> Result:

        try:
            tutor = self.repository.get_tutor_by_id(tutor_id)
            personal_tutor = PersonalTutor.from_tutor(tutor)
            if not PersonalTutorPolicy.can_assign_personal_tutor(
                user, personal_tutor.department
            ):
                return FailureResult(
                    message="You do not have permission to perform this action",
                    type_=ResponseTypes.PERMISSION_ERROR,
                )

            personal_tutor.training = Training.new_training(status="assigned")
            created_tutor = self.repository.create_personal_tutor(
                personal_tutor.serialise()
            )
            return SuccessResult(PersonalTutor(**created_tutor).serialise())
        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

    def update_tutor(
        self, user: AuthorisedUser, tutor_id: int, tutor_details: dict
    ) -> Result:
        try:
            tutor = PersonalTutor(**self.repository.get_personal_tutor_by_id(tutor_id))
            if not PersonalTutorPolicy.can_update_personal_tutor(
                user, tutor.email, tutor.department
            ):
                return FailureResult(
                    message="You do not have permission to perform this action",
                    type_=ResponseTypes.PERMISSION_ERROR,
                )

            tutor.update(tutor_details)
            updated_tutor = self.repository.update_personal_tutor(tutor.serialise())
            return SuccessResult(PersonalTutor(**updated_tutor).serialise())
        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )

    def get_schedule(
        self, user: AuthorisedUser, tutor_id: int, schedule: dict[str, str]
    ) -> Result: ...
