from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class NotificationStatus(str, Enum):
    SENT = "SENT"
    PENDING = "PENDING"
    FAILED = "FAILED"


class Notification(BaseModel):
    _id: int
    message: str
    created_at: datetime
    status: NotificationStatus


class Schedule(BaseModel):
    _id: int
    start_time: datetime
    end_time: datetime
