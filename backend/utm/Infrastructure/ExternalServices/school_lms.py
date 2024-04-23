from utm.core.Application.Common.interfaces import ISchoolLmsRepository
from faker import Faker

fake = Faker()

DB = {
    "academic_sessions": [
        {
            "id": "1",
            "name": "2020/2021",
            "start_date": fake.date_this_year().isoformat(),
            "end_date": fake.date_this_year().isoformat(),
        },
        {
            "id": "2",
            "name": "2021/2022",
            "start_date": fake.date_this_year().isoformat(),
            "end_date": fake.date_this_year().isoformat(),
        },
        {
            "id": "3",
            "name": "2022/2023",
            "start_date": fake.date_this_year().isoformat(),
            "end_date": fake.date_this_year().isoformat(),
        },
    ]
}


class MemorySchoolLms(ISchoolLmsRepository):

    def __init__(self, school_lms_data: dict):
        self.school_lms_data = school_lms_data

    @classmethod
    def from_fake(cls):
        return cls(DB)

    def set_resource_exception(self, resource_exception):
        self.resource_exception = resource_exception
        return self

    def get_academic_session(self, session_id: str) -> dict:
        for session in self.school_lms_data["academic_sessions"]:

            if session["id"] == session_id:
                return session
        raise self.resource_exception("Academic Session not found")

    def get_academic_sessions_by_ids(self, session_ids: list[str]) -> dict:
        return {
            session_id: self.get_academic_session(session_id)
            for session_id in session_ids
        }
