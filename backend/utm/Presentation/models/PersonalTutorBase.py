from pydantic import BaseModel


class PersonalTutorTraining(BaseModel):
    id: int = None
    status: str
    date: str = None


class PersonalTutorBase(BaseModel):
    id: int
    name: str
    email: str
    module: str
