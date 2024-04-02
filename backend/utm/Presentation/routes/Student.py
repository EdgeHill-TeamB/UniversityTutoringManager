from fastapi import APIRouter, Depends, status
from typing import Annotated
from ..models.common import Schedule
from ..models.meeting import RequestMeeting, RequestMeetingResponse
from ..common._exceptions import ResourceNotFoundException
from ..common.make_response import ResponseMaker
from ..dependencies.student import get_student_manager
from ..dependencies.authorisation import get_request_user
from utm.core.Application.Common.authorised_user import AuthorisedUser
from utm.core.Application.Student.interfaces import IStudentManager
from utm.core.Application.Meeting.interfaces import IMeetingManager
from utm.core.Application.Common.responses import Result


router = APIRouter()


@router.post("/{student_id}/request-meeting")
async def request_meeting(
    student_id: int,
    meeting: RequestMeeting,
    manager=Annotated[IMeetingManager, Depends(get_student_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.request_student_meeting(
        actor=user, student_id=student_id, meeting=meeting.model_dump()
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value,
        model_class=RequestMeetingResponse,
        status_code=status.HTTP_200_OK,
    )


@router.get("/{student_id}/schedule")
async def get_schedule(
    student_id: int,
    schedule: Schedule,
    manager=Annotated[IStudentManager, Depends(get_student_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_schedule(
        actor=user, student_id=student_id, schedule=schedule.model_dump()
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_list(
        data=result.value, model_class=Schedule, status_code=status.HTTP_200_OK
    )


# get students route

# notify student route
