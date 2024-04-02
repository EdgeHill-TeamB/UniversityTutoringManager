from pydantic import BaseModel


class Cohort(BaseModel):
    id: int
    title: str
    dept_id: int


class CohortFilter(BaseModel):
    id: int
    dept_id: int
