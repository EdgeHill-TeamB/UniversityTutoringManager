from typing import Protocol
from ..Common.responses import Result
from ..Common.authorised_user import AuthorisedUser


class IPersonalTutorManager(Protocol):

    def get_personal_tutors(self, actor: AuthorisedUser) -> Result: ...

    def get_personal_tutor_by_id(
        self, actor: AuthorisedUser, tutor_id: int
    ) -> Result: ...

    def assign_tutor_as_personal_tutor(
        self, actor: AuthorisedUser, tutor_id: int
    ) -> Result: ...

    def update_training_status(
        self, actor: AuthorisedUser, tutor_id: int, status: dict[str, str]
    ) -> Result: ...

    def get_schedule(
        self, actor: AuthorisedUser, tutor_id: int, schedule: dict[str, str]
    ) -> Result: ...
