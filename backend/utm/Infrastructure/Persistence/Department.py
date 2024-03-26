from utm.core.Application.Department.dept_manager import IDepartmentRepository


class MEMDepartmentRepo(IDepartmentRepository):

    def __init__(self, db: dict[str, str]):
        self.db = db

    def get_staff_by_department_id(self, deparment_id):
        if deparment_id not in self.db:
            return None
        return self.db[deparment_id]["Staff"]
