from pydantic import BaseModel


class StudentProfile(BaseModel):
    id: int
    name: str
    age: int
    email: str
    department: str


class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str
    department: str
