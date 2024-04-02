from fastapi import APIRouter, Depends, status
from typing import Annotated
from ..models.common import Schedule
from ..common._exceptions import ResourceNotFoundException
from ..common.make_response import ResponseMaker
from ..dependencies.personal_tutor import get_personal_tutor_manager
from ..dependencies.authorisation import get_request_user
from utm.core.Application.Common.authorised_user import AuthorisedUser
from utm.core.Application.PersonalTutor.interfaces import IPersonalTutorManager
from utm.core.Application.Common.responses import Result

router = APIRouter()


@router.get("/{tutor_id}/schedule")
async def get_schedule(
    tutor_id: int,
    schedule: Schedule,
    manager=Annotated[IPersonalTutorManager, Depends(get_personal_tutor_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_schedule(
        actor=user, tutor_id=tutor_id, schedule=schedule.model_dump()
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_list(
        data=result.value,
        model_class=Schedule,
        status_code=status.HTTP_200_OK,
    )
