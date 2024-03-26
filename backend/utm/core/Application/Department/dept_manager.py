from typing import Protocol

from ...Domain.DepartmentStaff import DepartmentStaff
from ..Common.responses import SuccessResult, FailureResult, ResponseTypes, Result
from ..Common._exceptions import UTMApplicationError


class IDepartmentRepository(Protocol):

    def set_resource_exception(exc: UTMApplicationError): ...

    def get_staff_by_department_id(department_id: str): ...


class IDepartmentManager(Protocol):

    def get_staff(self, department_id: int) -> Result: ...


class DepartmentManager:
    def __init__(self, repository: IDepartmentRepository):
        self.repository = repository

    def get_staff(self, department_id) -> Result:
        try:
            result = self.repository.get_staff_by_department_id(department_id)
            return SuccessResult(
                [DepartmentStaff(**staff).serialise() for staff in result]
            )
        except UTMApplicationError as exc:
            return FailureResult(
                message=exc,
                type_=ResponseTypes.RESOURCE_ERROR,
            )
