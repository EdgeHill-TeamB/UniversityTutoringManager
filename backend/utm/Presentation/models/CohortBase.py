from typing import List
from pydantic import BaseModel


class CohortBase(BaseModel):
    id: int
    name: str
    start_date: str
