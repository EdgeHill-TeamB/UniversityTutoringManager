from fastapi import APIRouter, Depends, status
from typing import Annotated
from ..models.common import Notification
from ..models.student import Student
from ..common._exceptions import ResourceNotFoundException
from ..common.make_response import ResponseMaker
from ..dependencies.student_cohort import get_cohort_manager
from ..dependencies.authorisation import get_request_user
from utm.core.Application.Common.authorised_user import AuthorisedUser
from utm.core.Application.Common.responses import Result
from utm.core.Application.StudentCohort.interfaces import ICohortManager
from utm.core.Application.Common.responses import Result

router = APIRouter()


@router.get("/{cohort_id}/students")
async def get_students(
    cohort_id: int,
    manager=Annotated[ICohortManager, Depends(get_cohort_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_cohort_students(cohort_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_list(
        data=result.value, model_class=Student, status_code=status.HTTP_200_OK
    )


@router.post("/notify/{cohort_id}")
async def send_notification(
    cohort_id: int,
    message: str,
    manager=Annotated[ICohortManager, Depends(get_cohort_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.notify(actor=user, cohort_id=cohort_id, message=message)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=Notification, status_code=status.HTTP_200_OK
    )
