from pydantic import BaseModel


class Staff(BaseModel):
    id: int
    name: str
    email: str
    office_no: str
    dept_id: int
    role: list[str]
    training_status: bool


class StaffFilter(BaseModel):
    id: int
    dept_id: int
