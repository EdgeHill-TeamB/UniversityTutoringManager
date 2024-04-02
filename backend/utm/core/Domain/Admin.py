from abc import ABC, abstractmethod


class Admin(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_cohort_meeting_record(self):
        pass


class DepartmentAdmin(Admin):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def view_student_records(self):
        # Logic to view student records within the department
        pass


class SchoolAdmin(Admin):
    def view_student_records(self):
        # Logic to view all student records
        pass
