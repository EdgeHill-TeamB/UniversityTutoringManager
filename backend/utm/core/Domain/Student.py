class Student:

    def __init__(self, student_id, name, email, password, role):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.password = password

    def get_attendance_record(self):
        pass

    def notify(self, message):
        pass

    def serialise(self) -> dict[str, str]:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
        }
