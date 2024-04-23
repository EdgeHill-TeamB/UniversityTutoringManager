from utm.core.Application.Common.interfaces import IDepartmentRepository
from faker import Faker
from faker.providers import DynamicProvider

departments_provider = DynamicProvider(
    provider_name="departments",
    elements=[
        "Computer Science",
        "Biological Science",
        "Medicine and Surgery",
        "Social Science",
    ],
)

training_status_provider = DynamicProvider(
    provider_name="training_status",
    elements=[
        "Not Started",
        "In Progress",
        "Completed",
    ],
)

fake = Faker()
# fake.add_provider(departments_provider)
fake.add_provider(training_status_provider)


DB_STRUCTURE = dict[str, dict[str, list[dict[str, str]]]]

DB = {
    dept_name: {
        "Admin": [
            {
                "id": str(fake.random_int(min=1000, max=9999)),
                "name": fake.name(),
                "email": fake.email(),
                "department": dept_name,
            }
            for _ in range(2)
        ],
        "Tutors": [
            {
                "id": str(fake.random_int(min=1000, max=9999)),
                "name": fake.name(),
                "email": fake.email(),
                "module": fake.job(),
                "is_personal_tutor": fake.boolean(),
                "department": dept_name,
            }
            for _ in range(2)
        ],
        "Academic Sessions": [
            {
                "id": str(fake.random_int(min=1000, max=9999)),
                "session": "2021/2022",
                "start_date": fake.date_this_century().isoformat(),
                "end_date": fake.date_this_century().isoformat(),
            }
        ],
        "Students": [
            {
                "id": str(st),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "department": dept_name,
                "academic_session": {"id": "1"},
                "module": fake.job(),
                "cohort": {
                    "id": str(fake.random_int(min=1000, max=9999)),
                    "name": fake.job(),
                    "start_date": fake.date_this_century().isoformat(),
                },
            }
            for st in range(10)
        ],
        "Cohorts": [
            {
                "id": str(fake.random_int(min=1000, max=9999)),
                "name": fake.job(),
                "start_date": fake.date_this_century().isoformat(),
                "department": dept_name,
                "academic_session": {
                    "id": "1",
                },
                "tutors": [
                    {
                        "id": "1",
                        "name": fake.name(),
                        "email": fake.email(),
                        "module": fake.job(),
                        "training": {
                            "id": str(fake.random_int(min=1000, max=9999)),
                            "status": fake.training_status(),
                            "date": fake.date_this_century().isoformat(),
                        },
                        "is_active": True,
                        "start_date": fake.date_this_century().isoformat(),
                        "end_date": fake.date_this_century().isoformat(),
                    }
                ],
                "students": [
                    {
                        "id": str(cst),
                        "first_name": fake.first_name(),
                        "last_name": fake.last_name(),
                        "email": fake.email(),
                        "module": fake.job(),
                    }
                    for cst in range(10)
                ],
            }
            for _ in range(2)
        ],
        "Personal Tutors": [
            {
                "id": str(pt),
                "name": fake.name(),
                "email": fake.email(),
                "department": dept_name,
                "module": fake.job(),
                "training": {
                    "id": str(fake.random_int(min=1000, max=9999)),
                    "status": fake.training_status(),
                    "date": fake.date_this_century().isoformat(),
                },
                "cohorts": [
                    {
                        "id": str(fake.random_int(min=1000, max=9999)),
                        "name": fake.job(),
                        "academic_session": {"id": "1"},
                        "start_date": fake.date_this_century().isoformat(),
                    }
                    for _ in range(2)
                ],
            }
            for pt in range(2)
        ],
    }
    for dept_name in departments_provider.elements
}

DB["Computer Science"]["Admin"].append(
    {
        "id": "1234",
        "name": "Samson Nwizugbe",
        "email": "samson6398@gmail.com",
        "department": "Computer Science",
    }
)


class MEMDepartmentRepo(IDepartmentRepository):

    @classmethod
    def from_dict(cls, db: DB_STRUCTURE) -> "MEMDepartmentRepo":
        return cls(db)

    @classmethod
    def from_fake(cls) -> "MEMDepartmentRepo":
        return cls(DB)

    def __init__(self, db: DB_STRUCTURE):
        self.db = db

    def set_resource_exception(self, resource_exception):
        self.resource_exception = resource_exception
        return self

    def get_admin_by_department_id(self, department_id) -> list[dict[str, str]]:
        if department_id not in self.db:
            raise self.resource_exception("Department does not Exist")
        return self.db.get(department_id, {}).get("Admin", [])

    def get_tutors_by_department_id(self, department_id) -> list[dict[str, str]]:
        if department_id not in self.db:
            raise self.resource_exception("Department does not Exist")
        return self.db.get(department_id, {}).get("Tutors", [])

    def get_students_by_department_id(
        self, department_id: str, filters: dict[str, str]
    ) -> list[dict[str, str]]:
        filters.pop("department", None)
        if department_id not in self.db:
            raise self.resource_exception("Department does not Exist")

        return self.db.get(department_id, {}).get("Students", [])

    def get_student_by_id(self, student_id: int) -> dict[str, str]:
        for dept in self.db.values():
            for student in dept.get("Students", []):
                if student["id"] == str(student_id):
                    return student

        raise self.resource_exception("Student does not Exist")

    def get_personal_tutor_by_student_id(self, student_id: int) -> dict[str, str]:
        return {
            "id": "1234",
            "name": "Joe Magneta",
            "email": "personal_tutortest@test.com",
        }

    def get_tutor_by_id(self, tutor_id: int) -> dict[str, str]:
        for dept in self.db.values():
            for tutor in dept.get("Tutors", []):
                if tutor["id"] == str(tutor_id):
                    return tutor

        raise self.resource_exception("Tutor does not Exist")

    def get_personal_tutors_by_department_id(
        self, department_id: str
    ) -> list[dict[str, str]]:
        if department_id not in self.db:
            raise self.resource_exception("Department does not Exist")
        return self.db.get(department_id, {}).get("Personal Tutors", [])

    def get_personal_tutor_by_id(self, tutor_id: int) -> dict[str, str]:
        for dept in self.db.values():
            for tutor in dept.get("Personal Tutors", []):
                if tutor["id"] == str(tutor_id):
                    return tutor

        raise self.resource_exception("Personal Tutor does not Exist")

    def create_personal_tutor(self, tutor: dict[str, str]) -> dict[str, str]:
        if tutor["department"] not in self.db:
            raise self.resource_exception("Department does not Exist")
        tutor["training"]["id"] = str(fake.random_int(min=1000, max=9999))
        self.db[tutor["department"]]["Personal Tutors"].append(tutor)
        return tutor

    def update_personal_tutor(self, tutor: dict[str, str]) -> dict[str, str]:
        if tutor["department"] not in self.db:
            raise self.resource_exception("Department does not Exist")
        for i, t in enumerate(self.db[tutor["department"]]["Personal Tutors"]):
            if t["id"] == tutor["id"]:
                tutor["training"]["id"] = str(fake.random_int(min=1000, max=9999))
                self.db[tutor["department"]]["Personal Tutors"][i] = tutor
                return tutor
        raise self.resource_exception("Personal Tutor does not Exist")

    def add_cohort(self, cohort: dict[str, str]):
        if cohort["department"] not in self.db:
            raise self.resource_exception("Department does not Exist")
        cohort["id"] = str(fake.random_int(min=1000, max=9999))
        self.db[cohort["department"]]["Cohorts"].append(cohort)
        return cohort

    def get_cohort(self, cohort_id: int) -> dict[str, str]:
        for dept in self.db.values():
            for cohort in dept.get("Cohorts", []):
                if cohort["id"] == str(cohort_id):
                    return cohort

        raise self.resource_exception("Cohort does not Exist")

    def get_cohorts(self, department_id: str) -> list[dict[str, str]]:
        if department_id not in self.db:
            raise self.resource_exception("Department does not Exist")
        return self.db.get(department_id, {}).get("Cohorts", [])

    def set_cohort_tutor(
        self, _id: str, department, cohort_tutor_data: dict[str, str]
    ) -> dict[str, str]:
        for cohort in self.db[department].get("Cohorts", []):
            if cohort["id"] == _id:
                cohort.get("tutors", []).append(cohort_tutor_data)
                return cohort
        raise self.resource_exception("Cohort does not Exist")

    def add_students_to_cohort(
        self, _id: str, department: str, cohort_students_data: dict[str, str]
    ) -> dict[str, str]:
        if department not in self.db:
            raise self.resource_exception("Department does not Exist")

        for cohort in self.db[department].get("Cohorts", []):
            if cohort["id"] == _id:
                cohort["students"].extend(cohort_students_data)
                return cohort
        raise self.resource_exception("Cohort does not Exist")
