from typing import Protocol

from ..Common.authorised_user import AuthorisedUser
from ..Common.responses import Result


class IMeetingRepository(Protocol):

    def get_meetings(self, department_id: int): ...

    def get_meeting_by_id(self, meeting_id: int): ...

    def get_meeting_attendees(self, meeting_id: int): ...

    def get_meeting_personal_tutors(self, meeting_id: int): ...


class IMeetingManager(Protocol):

    def create_student_meeting(
        self, actor: AuthorisedUser, meeting: dict[str, str]
    ) -> Result: ...

    def create_cohort_meeting(
        self, actor: AuthorisedUser, meeting: dict[str, str]
    ) -> Result: ...

    def get_meetings(
        self, actor: AuthorisedUser, meeting: dict[str, str]
    ) -> Result: ...

    def get_meeting_by_id(self, meeting_id: int) -> Result: ...

    def update_meeting(
        self, actor: AuthorisedUser, meeting_id: int, meeting: dict[str, str]
    ) -> Result: ...

    def update_meeting_attendee(
        self, actor: AuthorisedUser, meeting_id: int, attendee: dict[str, str]
    ) -> Result: ...

    def get_meeting_attendees(
        self, actor: AuthorisedUser, meeting_id: int
    ) -> Result: ...
