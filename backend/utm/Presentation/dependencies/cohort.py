from utm.core.Application.Cohort.interfaces import ICohortManager
from utm.core.Application.Cohort.manager import CohortManager
from utm.core.Application.Common._exceptions import UTMApplicationError
from utm.Infrastructure.Persistence.Department import MEMDepartmentRepo
from utm.Infrastructure.ExternalServices.school_lms import MemorySchoolLms


def get_cohort_manager() -> ICohortManager:
    repository = MEMDepartmentRepo.from_fake().set_resource_exception(
        UTMApplicationError
    )
    school_lms = MemorySchoolLms.from_fake().set_resource_exception(UTMApplicationError)
    return CohortManager(repository=repository, school_lms=school_lms)
