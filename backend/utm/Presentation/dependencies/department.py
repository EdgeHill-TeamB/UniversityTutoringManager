from utm.core.Application.Department.manager import DepartmentManager
from utm.core.Application.Common._exceptions import UTMApplicationError
from utm.Infrastructure.Persistence.Department import MEMDepartmentRepo
from utm.Infrastructure.ExternalServices.school_lms import MemorySchoolLms


def get_dept_manager() -> DepartmentManager:
    school_lms = MemorySchoolLms.from_fake().set_resource_exception(UTMApplicationError)
    repo = MEMDepartmentRepo.from_fake().set_resource_exception(UTMApplicationError)
    manager = DepartmentManager(repository=repo, school_lms=school_lms)
    return manager
