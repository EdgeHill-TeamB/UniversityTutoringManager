from utm.core.Application.Department.Interfaces import IDepartmentRepository


class MEMDepartmentRepo(IDepartmentRepository):

    @classmethod
    def from_dict(cls, db: dict[str, str]) -> "MEMDepartmentRepo":
        return cls(db)

    def __init__(self, db):
        self.db = db

    def set_resource_exception(self, resource_exception):
        self.resource_exception = resource_exception
        return self

    def get_staff_by_department_id(self, department_id):
        if department_id not in self.db:
            raise self.resource_exception("Department does not Exist")
        return self.db[department_id]["Staff"]
