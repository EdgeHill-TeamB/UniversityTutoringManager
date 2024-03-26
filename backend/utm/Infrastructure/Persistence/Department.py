from utm.core.Application.Department.dept_manager import IDepartmentRepository


class MEMDepartmentRepo(IDepartmentRepository):

    @classmethod
    def from_dict(cls, db: dict[str, str]) -> "MEMDepartmentRepo":
        return cls(db)

    def __init__(self, db):
        self.db = db

    def set_resource_exception(self, resource_exception):
        self.resource_exception = resource_exception
        return self

    def get_staff_by_department_id(self, deparment_id):
        if deparment_id not in self.db:
            raise self.resource_exception("Deparment does not Exist")
        return self.db[deparment_id]["Staff"]
