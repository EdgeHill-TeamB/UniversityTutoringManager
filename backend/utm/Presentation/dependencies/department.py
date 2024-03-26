from utm.core.Application.Department.dept_manager import DepartmentManager
from utm.Infrastructure.Persistence.Department import MEMDepartmentRepo


def get_dept_manager() -> DepartmentManager:
    repo = MEMDepartmentRepo({})
    manager = DepartmentManager(repository=repo)
    return manager
