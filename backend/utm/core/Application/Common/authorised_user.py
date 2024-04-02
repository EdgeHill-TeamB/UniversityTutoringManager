class AuthorisedUser:

    def __init__(self, user_id: str, user_group: str, department_id: str):
        self._user_id = user_id
        self._user_group = user_group
        self._department_id = department_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def user_group(self):
        return self._user_group

    @property
    def department_id(self):
        return self._department_id

    def serialise(self) -> dict[str, str]:
        return {
            "user_id": self.user_id,
            "user_group": self.user_group,
            "department_id": self.department_id,
        }
