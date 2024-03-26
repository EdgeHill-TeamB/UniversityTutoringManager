from fastapi import APIRouter, Depends
from ..common.make_response import ErrorResponse
from ..models.staff import Staff
from ..dependencies.department import get_dept_manager
from typing import Annotated
from utm.core.Application.Department.dept_manager import IDepartmentManager

router = APIRouter()


@router.get("/department/staff")
async def get_staff(
    dept_id: int, manager=Annotated[IDepartmentManager, Depends(get_dept_manager)]
):
    staff_list = manager.get_staff()
    # return make_response(staff_list, Staff)
