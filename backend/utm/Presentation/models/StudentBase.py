from pydantic import BaseModel


class StudentBase(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    module: str


class CohortStudent(StudentBase):

    def __post_init__(self):
        is_true = True
