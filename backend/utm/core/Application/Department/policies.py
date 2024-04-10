from utm.core.Domain.DepartmentAdmin import DepartmentAdmin
from ..Common.authorised_user import AuthorisedUser


class ProfileViewPolicy:

    @classmethod
    def can_view_members(cls, user: AuthorisedUser):
        return user.user_group in ["Admin"]
