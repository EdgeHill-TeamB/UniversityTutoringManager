from datetime import datetime
from typing import List
from pydantic import BaseModel
from .student import Student
from enum import Enum


class MeetingStatus(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class CreateStudentMeeting(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str
    meeting_link: str
    meeting_password: str
    meeting_id: str
    meeting_duration: int
    meeting_host: str
    meeting_attendee: Student
    meeting_agenda: str


class CreateCohortMeeting(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str
    meeting_link: str
    meeting_password: str
    meeting_id: str
    meeting_duration: int
    meeting_host: str
    meeting_attendees: List[Student]
    meeting_agenda: str


class Meeting(BaseModel):
    id: int
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str
    meeting_link: str
    meeting_password: str
    meeting_id: str
    meeting_status: MeetingStatus
    meeting_duration: int
    meeting_host: str
    meeting_attendees: List[Student]
    meeting_agenda: str


class MeetingAttendee(BaseModel):
    id: int
    name: str
    age: int
    email: str
    department: str


class RequestMeeting(BaseModel):
    meeting_id: int
    meeting_attendee: Student


class RequestMeetingResponse(BaseModel):
    meeting_id: int
    meeting_attendee: Student
    status: str
