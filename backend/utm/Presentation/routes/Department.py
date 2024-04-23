from fastapi import APIRouter, Depends, status, Request
from ..common.make_response import ResponseMaker
from ..common._exceptions import ERRORS
from ..dependencies.authorisation import get_request_user
from ..dependencies.department import get_dept_manager
from ..dependencies.personal_tutor import get_personal_tutor_manager
from ..dependencies.cohort import get_cohort_manager
from ..models.department import DepartmentAdminModel, DepartmentTutorModel
from ..models.student import StudentProfile, AddStudentsToCohort
from ..models.personal_tutor import PersonalTutor, PersonalTutorUpdate
from ..models.cohort import CohortProfile, CohortCreate
from typing import Annotated, List
from utm.core.Application.Department.interfaces import IDepartmentManager
from utm.core.Application.PersonalTutor.interfaces import IPersonalTutorManager
from utm.core.Application.Cohort.interfaces import ICohortManager
from utm.core.Application.Common.authorised_user import AuthorisedUser
from utm.core.Application.Common.responses import Result

router = APIRouter()


@router.get("/staff")
async def get_staff(
    manager: Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):

    result: Result = manager.get_staff(user=user)

    if not result:
        raise ERRORS[result.type](detail=result.value)

    return ResponseMaker.from_multitype(
        data=result.value,
        model_classes={"admin": DepartmentAdminModel, "tutors": DepartmentTutorModel},
        status_code=status.HTTP_200_OK,
    )
    # Status => FUNCTIONALITY COMPLETE


@router.get("/students")
async def get_students(
    request: Request,
    manager: Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):

    filters = dict(request.query_params)
    result: Result = manager.get_students(user=user, filters=filters)
    if not result:
        raise ERRORS[result.type](detail=result.value)

    return ResponseMaker.from_list(
        data=result.value, model_class=StudentProfile, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.get("/students/{student_id}")
async def get_student_by_id(
    student_id: str,
    manager: Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_student_by_id(user=user, student_id=student_id)
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=StudentProfile, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.get("/tutors")
async def get_tutors(
    manager: Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_tutors(user=user)
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_list(
        data=result.value,
        model_class=DepartmentTutorModel,
        status_code=status.HTTP_200_OK,
    )
    # Status => FUNCTIONALITY COMPLETE


@router.get("/tutors/{tutor_id}")
async def get_tutor_by_id(
    tutor_id: int,
    manager: Annotated[IDepartmentManager, Depends(get_dept_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_tutor_by_id(user=user, tutor_id=tutor_id)
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_dict(
        data=result.value,
        model_class=DepartmentTutorModel,
        status_code=status.HTTP_200_OK,
    )
    # Status => FUNCTIONALITY COMPLETE


@router.get("/personal-tutors")
async def get_personal_tutors(
    manager: Annotated[IPersonalTutorManager, Depends(get_personal_tutor_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_personal_tutors(user=user)
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_list(
        data=result.value, model_class=PersonalTutor, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.post("/personal-tutors/{tutor_id}")
async def assign_as_personal_tutor(
    tutor_id: int,
    manager: Annotated[IPersonalTutorManager, Depends(get_personal_tutor_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.assign_tutor_as_personal_tutor(
        tutor_id=tutor_id, user=user
    )
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=PersonalTutor, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.get("/personal-tutors/{tutor_id}")
async def get_personal_tutor(
    tutor_id: int,
    manager: Annotated[IPersonalTutorManager, Depends(get_personal_tutor_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_personal_tutor(user=user, tutor_id=tutor_id)
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=PersonalTutor, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.patch("/personal-tutors/{tutor_id}")
async def update_tutor(
    tutor_id: int,
    tutor_update: PersonalTutorUpdate,
    manager: Annotated[IPersonalTutorManager, Depends(get_personal_tutor_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.update_tutor(
        user=user, tutor_id=tutor_id, tutor_details=tutor_update.model_dump()
    )
    if not result:
        raise ERRORS[result.type](detail=result.value)

    return ResponseMaker.from_dict(
        data=result.value,
        model_class=PersonalTutor,
        status_code=status.HTTP_200_OK,
    )
    # Status => FUNCTIONALITY COMPLETE


@router.post("/cohorts")
async def create_cohort(
    cohort: CohortCreate,
    manager: Annotated[ICohortManager, Depends(get_cohort_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.create_cohort(user=user, cohort_data=cohort.model_dump())
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=CohortProfile, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.get("/cohorts")
async def get_cohorts(
    manager: Annotated[ICohortManager, Depends(get_cohort_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_cohorts(user=user)
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_list(
        data=result.value, model_class=CohortProfile, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.get("/cohorts/{cohort_id}")
async def get_cohort_by_id(
    cohort_id: int,
    manager: Annotated[ICohortManager, Depends(get_cohort_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.get_cohort(user=user, cohort_id=cohort_id)
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=CohortProfile, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.post("/cohorts/{cohort_id}/students")
async def assign_students_to_cohort(
    cohort_id: int,
    students: AddStudentsToCohort,
    manager: Annotated[ICohortManager, Depends(get_cohort_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    students_list = students.model_dump().get("student_ids")
    result: Result = manager.add_students_to_cohort(
        cohort_id=cohort_id, user=user, students=students_list
    )
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=CohortProfile, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE


@router.post("/cohorts/{cohort_id}/personal-tutor/{tutor_id}")
async def assign_personal_tutor_to_cohort(
    cohort_id: int,
    tutor_id: int,
    manager: Annotated[ICohortManager, Depends(get_cohort_manager)],
    user: Annotated[AuthorisedUser, Depends(get_request_user)],
):
    result: Result = manager.assign_personal_tutor_to_cohort(
        cohort_id=cohort_id, personal_tutor_id=tutor_id, user=user
    )
    if not result:
        raise ERRORS[result.type](detail=result.value)
    return ResponseMaker.from_dict(
        data=result.value, model_class=CohortProfile, status_code=status.HTTP_200_OK
    )
    # Status => FUNCTIONALITY COMPLETE
