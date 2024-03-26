from pydantic import BaseModel


class AuthResponse(BaseModel):

    first_name: str
    last_name: str
    email: str
    credentials: str

    def to_json(self) -> dict[str, str]:
        return self.model_dump_json()
