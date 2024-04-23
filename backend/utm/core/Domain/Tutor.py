class Tutor:
    def __init__(self, id, name, module, email, department, is_personal_tutor):
        self.id = id
        self.name = name
        self.module = module
        self.email = email
        self.is_personal_tutor = is_personal_tutor
        self.department = department

    def get_name(self):
        return self.name

    def get_module(self):
        return self.module

    def get_department(self):
        return self.department

    def serialise(self) -> dict[str, str]:
        return {
            "id": self.id,
            "name": self.name,
            "module": self.module,
            "email": self.email,
            "department": self.department,
            "is_personal_tutor": self.is_personal_tutor,
        }
