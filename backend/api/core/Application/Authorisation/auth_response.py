from dataclasses import dataclass


@dataclass
class AuthResponse:

    first_name: str
    last_name: str
    email: str
    credentials: str
