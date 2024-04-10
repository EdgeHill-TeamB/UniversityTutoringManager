class Tutor:
    def __init__(self, id, name, module, email, training_status, department):
        self.id = id
        self.name = name
        self.module = module
        self.email = email
        self.personal_tutor_training_status = training_status
        self.department = department

    def get_name(self):
        return self.name

    def get_module(self):
        return self.module

    def get_department(self):
        return self.department

    def get_personal_tutor_training_status(self):
        return self.personal_tutor_training_status

    def set_personal_tutor_training_status(self, status):
        self.personal_tutor_training_status = status

    def serialise(self) -> dict[str, str]:
        return {
            "id": self.id,
            "name": self.name,
            "module": self.module,
            "email": self.email,
            "training_status": self.personal_tutor_training_status,
            "department": self.department,
        }
