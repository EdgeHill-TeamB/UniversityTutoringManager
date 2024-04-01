from fastapi import APIRouter, Depends, status
from ..common.make_response import ResponseMaker
from ..common._exceptions import ResourceNotFoundException
from ..models.staff import Staff
from ..models.cohort import Cohort
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


### Update a staff's role to personal tutor
@router.put("/make-tutor")
async def make_tutor(
    staff_id: int, manager=Annotated[IDepartmentManager, Depends(get_dept_manager)]
):
    result: Result = manager.get_staff(staff_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    result.update({"role": "personal tutor"})
    return ResponseMaker.from_dict(
        data=result.value, model_class=Staff, status_code=status.HTTP_200_OK
    )


### Update a tutor's training status
@router.put("/training-status")
async def update_training_status(
    staff_id: int, manager=Annotated[IDepartmentManager, Depends(get_dept_manager)]
):
    result: Result = manager.get_staff(staff_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    
    if result.training_status == True:
        result.training_status == False
        return ResponseMaker(
        data="Updated Successfully", status_code=status.HTTP_200_OK
    ) 
    else:
        result.training_status == True
        return ResponseMaker(
        data="Updated Successfully", status_code=status.HTTP_200_OK
    ) 


### Create a cohort
@router.post("/create-cohort")
async def create_cohort(
    dept_id: int, cohort: Cohort
):
    cohort_dict = cohort.model_dump()
    cohort_dict.update({"dept_id": dept_id})
    return ResponseMaker(
        data="Cohort created successfully", status_code=status.HTTP_200_OK
    )
    

### Assign a tutor to a cohort
@router.post("/assign-tutor")
async def assign_tutor(
    staff_id: int, cohort_id: int, manager=Annotated[IDepartmentManager, Depends(get_dept_manager)]
):
    staff: Result = manager.get_staff(staff_id)
    if not staff:
        raise ResourceNotFoundException(staff.value)
    
    staff.update({"cohort_id": cohort_id})
    return ResponseMaker(
        data="Personal tutor assigned successfully", status_code=status.HTTP_200_OK
    )


### Get all students and select the ones you want to add to a cohort 
@router.post("/students-cohort")
async def students_cohort(
    dept_id: int, cohort_id: int, manager=Annotated[IDepartmentManager, Depends(get_dept_manager)]
):
    students: Result = manager.get_students(dept_id)
    if not students:
        raise ResourceNotFoundException(students.value)
    
    students.update({"cohort_id": cohort_id})
    return ResponseMaker(
        data="Students added to cohort successfully", status_code=status.HTTP_200_OK
    )
