from utm.core.Application.Department.Interfaces import IDepartmentRepository
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
                "training_status": fake.training_status(),
                "department": dept_name,
            }
            for _ in range(2)
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
