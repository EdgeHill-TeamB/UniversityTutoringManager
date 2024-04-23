from datetime import datetime


class Training:

    def __init__(self, status: str, date: str, id=None):
        self.id = id
        self.status = status
        self.date = datetime.strptime(date, "%Y-%m-%d")

    @classmethod
    def new_training(cls, status: str):
        return cls(status=status, date=datetime.now().strftime("%Y-%m-%d"))

    def serialise(self) -> dict[str, str]:
        return {
            "id": self.id,
            "status": self.status,
            "date": self.date.strftime("%Y-%m-%d"),
        }


class PersonalTutorBase:
    def __init__(
        self,
        id,
        name,
        email,
        module,
        training: Training = None,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.module = module
        if training is not None:
            self.training = Training(**training)

    @classmethod
    def from_tutor(cls, tutor: dict):
        training = tutor.get("training", None) if hasattr(tutor, "training") else None
        return cls(
            id=tutor["id"],
            name=tutor["name"],
            email=tutor["email"],
            department=tutor["department"],
            module=tutor["module"],
            training=Training(**training) if training is not None else None,
        )

    def update(self, details: dict):
        email = details.get("email", None)
        if email is not None:
            self.email = email
        if "training" in details:
            details["training"]["date"] = datetime.now().strftime("%Y-%m-%d")
        self.training = Training(**details.get("training", self.training.serialise()))

    def serialise(self) -> dict[str, str]:
        result = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "module": self.module,
            "training": self.training.serialise(),
        }
        return result
