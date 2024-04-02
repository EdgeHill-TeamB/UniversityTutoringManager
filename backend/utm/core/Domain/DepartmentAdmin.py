class DepartmentAdmin:
    def __init__(self, department_name):
        self.department_name = department_name

    def make_personal_tutor(self, tutor):
        tutor.is_personal_tutor = True
        # Add any additional logic here

    def assign_cohort_to_tutors(self, cohort, tutors):
        for tutor in tutors:
            tutor.cohort = cohort
        # Add any additional logic here

    def serialise(self) -> dict[str, str]: ...
