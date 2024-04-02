from utm.core.Domain.DepartmentAdmin import DepartmentAdmin
from ..Common.authorised_user import AuthorisedUser


class ProfileViewPolicy:

    @classmethod
    def can_view_members(cls, user: AuthorisedUser, department_id):
        return user.user_group in ["Admin"] and user.department_id == department_id
