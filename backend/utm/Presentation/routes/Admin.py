from fastapi import APIRouter, Depends, status
from ..common.make_response import ResponseMaker
from ..common._exceptions import ResourceNotFoundException
from ..dependencies.authorisation import get_request_user
from ..dependencies.department import get_dept_manager
from ..models.department import DepartmentAdminModel, DepartmentTutorModel
from ..models.student import StudentProfile, Student
from ..models.personal_tutor import PersonalTutor, PersonalTutorTrainingStatus
from ..models.student_cohort import Cohort
from typing import Annotated, List
from utm.core.Application.Department.Interfaces import IDepartmentManager, TutorEnum
from utm.core.Application.PersonalTutor.interfaces import IPersonalTutorManager
from utm.core.Application.StudentCohort.interfaces import ICohortManager
from utm.core.Application.Common.authorised_user import AuthorisedUser
from utm.core.Application.Common.responses import Result

router = APIRouter()


@router.get("/staff")
async def get_staff(
    dept_id: int,
    manager=Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_staff(actor=user, department_id=dept_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_multitype(
        data=result.value,
        model_classes={"admin": DepartmentAdminModel, "tutors": DepartmentTutorModel},
        status_code=status.HTTP_200_OK,
    )


@router.get("/students")
async def get_students(
    dept_id: int,
    manager=Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_students(actor=user, department_id=dept_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_list(
        data=result.value, model_class=StudentProfile, status_code=status.HTTP_200_OK
    )


@router.get("/students/{student_id}")
async def get_student_by_id(
    student_id: int,
    manager=Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_student_by_id(actor=user, student_id=student_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=StudentProfile, status_code=status.HTTP_200_OK
    )


@router.post("/tutors")
async def get_tutors(
    dept_id: int,
    tutor_status: TutorEnum = TutorEnum.all,
    manager=Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_tutors(
        department_id=dept_id, actor=user, status=tutor_status
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_list(
        data=result.value,
        model_class=DepartmentTutorModel,
        status_code=status.HTTP_200_OK,
    )


@router.get("/tutors/{tutor_id}")
async def get_tutor_by_id(
    tutor_id: int,
    manager=Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_tutor_by_id(actor=user, tutor_id=tutor_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value,
        model_class=DepartmentTutorModel,
        status_code=status.HTTP_200_OK,
    )


@router.post("/personal-tutors/{tutor_id}")
async def assign_as_personal_tutor(
    tutor_id: int,
    manager=Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.assign_tutor_as_personal_tutor(
        tutor_id=tutor_id, actor=user
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=PersonalTutor, status_code=status.HTTP_200_OK
    )


@router.get("/personal-tutors/{tutor_id}/training-status")
async def get_tutor_training_status(
    tutor_id: int,
    manager=Annotated[IPersonalTutorManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_training_status(actor=user, tutor_id=tutor_id)
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value,
        model_class=PersonalTutorTrainingStatus,
        status_code=status.HTTP_200_OK,
    )


@router.put("/personal-tutors/{tutor_id}/training-status")
async def update_tutor_training_status(
    tutor_id: int,
    training_status: PersonalTutorTrainingStatus,
    manager=Annotated[IPersonalTutorManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.update_training_status(
        actor=user, tutor_id=tutor_id, training_status=training_status.model_dump()
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value,
        model_class=PersonalTutorTrainingStatus,
        status_code=status.HTTP_200_OK,
    )


@router.post("/cohorts")
async def create_cohort(
    cohort: Cohort,
    manager=Annotated[ICohortManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.create_cohort(actor=user, cohort=cohort.model_dump())
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=Cohort, status_code=status.HTTP_200_OK
    )


@router.post("/cohorts/{cohort_id}/students")
async def assign_students_to_cohort(
    cohort_id: int,
    students: List[Student],
    manager=Annotated[ICohortManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    students_list = [student.model_dump() for student in students]
    result: Result = manager.assign_students_to_cohort(
        cohort_id, actor=user, students=students_list
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=Cohort, status_code=status.HTTP_200_OK
    )


@router.post("/cohorts/{cohort_id}/personal-tutor/{tutor_id}")
async def assign_personal_tutor_to_cohort(
    cohort_id: int,
    tutor_id: int,
    manager=Annotated[ICohortManager, Depends(get_dept_manager)],
    user=Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.assign_personal_tutor_to_cohort(
        cohort_id, tutor_id, actor=user
    )
    if not result:
        raise ResourceNotFoundException(result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=Cohort, status_code=status.HTTP_200_OK
    )
