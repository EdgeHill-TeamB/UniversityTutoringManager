from typing import Protocol

from ...Domain.DepartmentStaff import DepartmentStaff


class IDepartmentRepository(Protocol):

    def get_staff_by_department_id(department_id: str): ...


class IDepartmentManager(Protocol):

    def get_staff(self, department_id) -> list[DepartmentStaff]: ...


class DepartmentManager:
    def __init__(self, repository: IDepartmentRepository):
        self.repository = repository

    def get_staff(self, department_id) -> list[DepartmentStaff]:
        result = self.repository.get_staff_by_department_id(department_id)
        if result:
            return [DepartmentStaff(staff) for staff in result]
        return []
