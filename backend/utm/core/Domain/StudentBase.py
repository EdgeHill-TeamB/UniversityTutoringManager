class StudentBase:

    def __init__(
        self,
        id: str,
        first_name: str = None,
        last_name: str = None,
        email: str = None,
        module: str = None,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.module = module

    def serialise(self) -> dict[str, str]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "module": self.module,
        }
