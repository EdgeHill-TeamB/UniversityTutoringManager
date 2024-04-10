from pydantic import BaseModel


class DepartmentModel(BaseModel):
    id: int
    name: str
    description: str

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


class DepartmentAdminModel(BaseModel):
    id: str
    name: str
    email: str
    department: str

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
        }


class DepartmentTutorModel(BaseModel):
    id: str
    name: str
    email: str
    module: str
    training_status: str
    department: str

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "module": self.module,
            "training_status": self.training_status,
            "department": self.department,
        }
