from utm.core.Application.Department.dept_manager import DepartmentManager
from utm.core.Application.Common._exceptions import UTMApplicationError
from utm.Infrastructure.Persistence.Department import MEMDepartmentRepo


def get_dept_manager() -> DepartmentManager:
    repo = MEMDepartmentRepo.from_dict({}).set_resource_exception(UTMApplicationError)
    manager = DepartmentManager(repository=repo)
    return manager
