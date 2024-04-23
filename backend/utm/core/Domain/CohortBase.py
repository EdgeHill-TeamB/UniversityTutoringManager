from datetime import datetime
from .AcademicSession import AcademicSession


class CohortBase:
    def __init__(
        self,
        name: str,
        start_date: str,
        academic_session: dict[str, str],
        id: str = None,
    ):

        self.id = id
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.name = name
        self.academic_session = AcademicSession(**academic_session)

    def serialise(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "academic_session": self.academic_session.serialise(),
        }
