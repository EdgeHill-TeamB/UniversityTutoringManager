from typing import Protocol
from ..Common.responses import Result
from ..Common.authorised_user import AuthorisedUser


class IPersonalTutorRepository(Protocol):

    def get_personal_tutors(self, department_id: int): ...

    def get_personal_tutor_by_id(self, tutor_id: int): ...

    def get_personal_tutor_assignments(self, department_id: int): ...

    def assign_personal_tutor(self, department_id: int, tutor_id: int): ...

    def unassign_personal_tutor(self, department_id: int, tutor_id: int): ...


class IPersonalTutorManager(Protocol):

    def get_training_status(self, actor: AuthorisedUser, tutor_id: int) -> Result: ...

    def update_training_status(
        self, actor: AuthorisedUser, tutor_id: int, status: dict[str, str]
    ) -> Result: ...

    def get_schedule(
        self, actor: AuthorisedUser, tutor_id: int, schedule: dict[str, str]
    ) -> Result: ...
