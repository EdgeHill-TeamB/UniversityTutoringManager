from utm.core.Application.PersonalTutor.interfaces import IPersonalTutorManager
from utm.core.Application.PersonalTutor.manager import PersonalTutorManager
from utm.core.Application.Common._exceptions import UTMApplicationError
from utm.Infrastructure.Persistence.Department import MEMDepartmentRepo


def get_personal_tutor_manager() -> IPersonalTutorManager:
    repo = MEMDepartmentRepo.from_fake().set_resource_exception(UTMApplicationError)
    return PersonalTutorManager(repository=repo)
