class Tutor:
    def __init__(self, name, module, department):
        self.name = name
        self.module = module
        self.personal_tutor_training_status = False

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
            "name": self.name,
            "module": self.module,
            "personal_tutor_training_status": self.personal_tutor_training_status,
        }
