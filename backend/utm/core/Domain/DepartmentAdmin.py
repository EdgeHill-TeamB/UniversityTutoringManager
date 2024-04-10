class DepartmentAdmin:
    def __init__(self, id, name, email, department):
        self.id = id
        self.name = name
        self.email = email
        self.department = department

    def make_personal_tutor(self, tutor):
        tutor.is_personal_tutor = True
        # Add any additional logic here

    def assign_cohort_to_tutors(self, cohort, tutors):
        for tutor in tutors:
            tutor.cohort = cohort
        # Add any additional logic here

    def serialise(self) -> dict[str, str]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
        }
