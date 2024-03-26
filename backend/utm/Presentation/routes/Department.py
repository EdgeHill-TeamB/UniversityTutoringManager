from fastapi import APIRouter, Depends, status
from ..common.make_response import ResponseMaker
from ..common._exceptions import ResourceNotFoundException
from ..models.staff import Staff
from ..dependencies.department import get_dept_manager
from typing import Annotated
from utm.core.Application.Department.dept_manager import IDepartmentManager
from utm.core.Application.Common.responses import Result

router = APIRouter()


@router.get("/staff")
async def get_staff(
    dept_id: int, manager=Annotated[IDepartmentManager, Depends(get_dept_manager)]
):
    result: Result = manager.get_staff(dept_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_list(
        data=result.value, model_class=Staff, status_code=status.HTTP_200_OK
    )
