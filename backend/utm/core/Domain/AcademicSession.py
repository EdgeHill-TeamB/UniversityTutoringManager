from datetime import datetime


class AcademicSession:
    def __init__(
        self, id: str, name: str = None, start_date: str = None, end_date: str = None
    ):

        self.id = id
        self.name = name
        self.start_date = (
            datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
        )
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    def set_session_data(self, session_data: dict[str, str]):
        self.name = session_data.get("name", None)
        self.start_date = (
            datetime.strptime(session_data["start_date"], "%Y-%m-%d")
            if session_data.get("start_date", None)
            else None
        )
        self.end_date = (
            datetime.strptime(session_data["end_date"], "%Y-%m-%d")
            if session_data.get("end_date", None)
            else None
        )

    def serialise(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": (
                self.start_date.strftime("%Y-%m-%d") if self.start_date else None
            ),
            "end_date": self.end_date.strftime("%Y-%m-%d") if self.end_date else None,
        }
