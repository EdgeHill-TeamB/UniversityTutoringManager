from .PersonalTutorBase import PersonalTutorBase, Training
from .CohortBase import CohortBase


class PersonalTutor(PersonalTutorBase):
    def __init__(
        self,
        name: str,
        email: str,
        department: str,
        module: str,
        training,
        cohorts: list[dict[str, str]],
        id: str = None,
    ):
        super().__init__(id, name, email, module, training)
        self.department = department
        self.cohorts = [CohortBase(**cohort) for cohort in cohorts]

    @classmethod
    def from_tutor(cls, tutor: dict):
        training = tutor.get("training", None) if hasattr(tutor, "training") else None
        return cls(
            id=tutor["id"],
            name=tutor["name"],
            email=tutor["email"],
            department=tutor["department"],
            module=tutor["module"],
            cohorts=[CohortBase(**cohort) for cohort in tutor.get("cohorts", [])],
            training=Training(**training) if training is not None else None,
        )

    def serialise(self):
        result = {
            **super().serialise(),
            "department": self.department,
            "cohorts": [cohort.serialise() for cohort in self.cohorts],
        }
        return result


class CohortPersonalTutor(PersonalTutorBase):
    def __init__(
        self,
        id,
        name,
        email,
        module,
        training: dict[str, str] = None,
        is_active: bool = None,
        start_date: str = None,
        end_date: str = None,
    ):
        super().__init__(id, name, email, module, training)
        self.is_active = is_active
        self.start_date = start_date
        self.end_date = end_date

    @classmethod
    def from_personal_tutor(cls, tutor: PersonalTutor):
        return cls(
            id=tutor.id,
            name=tutor.name,
            email=tutor.email,
            module=tutor.module,
            training=tutor.training.serialise() if tutor.training is not None else None,
        )

    def serialise(self, include_active=False) -> dict[str, str]:
        super_data = super().serialise()
        super_data = super_data if super_data is not None else {}
        result = {
            **super_data,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
        if include_active:
            result["is_active"] = self.is_active
        return result
