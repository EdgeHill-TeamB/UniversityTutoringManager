from typing import Annotated
from fastapi import APIRouter, Depends, status
from ..dependencies.authorisation import get_request_user
from ..dependencies.meeting import get_meeting_manager
from ..models.meeting import (
    CreateCohortMeeting,
    CreateStudentMeeting,
    Meeting,
    MeetingAttendee,
)
from ..common.make_response import ResponseMaker
from ..common._exceptions import ResourceNotFoundException
from utm.core.Application.Meeting.interfaces import IMeetingManager
from utm.core.Application.Common.authorised_user import AuthorisedUser
from utm.core.Application.Common.responses import Result


router = APIRouter()


@router.get("/")
async def get_meetings(
    meeting: Meeting,
    manager=Annotated[IMeetingManager, Depends(get_meeting_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_meetings(actor=user, meeting=meeting.model_dump())
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_list(
        data=result.value, model_class=Meeting, status_code=status.HTTP_200_OK
    )


@router.post("/students")
async def create_student_meeting(
    meeting: CreateStudentMeeting,
    manager=Annotated[IMeetingManager, Depends(get_meeting_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.create_student_meeting(
        actor=user, meeting=meeting.model_dump()
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=Meeting, status_code=status.HTTP_200_OK
    )


@router.post("/cohorts")
async def create_cohort_meeting(
    meeting: CreateCohortMeeting,
    manager=Annotated[IMeetingManager, Depends(get_meeting_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.create_cohort_meeting(
        actor=user, meeting=meeting.model_dump()
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=Meeting, status_code=status.HTTP_200_OK
    )


@router.get("/{meeting_id}")
async def get_meeting_by_id(
    meeting_id: int,
    manager=Annotated[IMeetingManager, Depends(get_meeting_manager)],
):
    result: Result = manager.get_meeting_by_id(meeting_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=Meeting, status_code=status.HTTP_200_OK
    )


@router.put("/{meeting_id}")
async def update_meeting(
    meeting_id: int,
    meeting: Meeting,
    manager=Annotated[IMeetingManager, Depends(get_meeting_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.update_meeting(
        actor=user, meeting_id=meeting_id, meeting=meeting
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=Meeting, status_code=status.HTTP_200_OK
    )


@router.put("/{meeting_id}/attendee")
async def update_meeting_attendee(
    meeting_id: int,
    attendee: MeetingAttendee,
    manager=Annotated[IMeetingManager, Depends(get_meeting_manager)],
):
    result: Result = manager.update_attendee_record(meeting_id, attendee)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=MeetingAttendee, status_code=status.HTTP_200_OK
    )


@router.get("/{meeting_id}/attendees")
async def get_meeting_attendees(
    meeting_id: int,
    manager=Annotated[IMeetingManager, Depends(get_meeting_manager)],
):
    result: Result = manager.get_meeting_attendees(meeting_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_list(
        data=result.value, model_class=MeetingAttendee, status_code=status.HTTP_200_OK
    )
