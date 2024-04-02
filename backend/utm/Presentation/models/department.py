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
    id: int
    name: str
    email: str
    phone: str

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }


class DepartmentTutorModel(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    def model_dump(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }
