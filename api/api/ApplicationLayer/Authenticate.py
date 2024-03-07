from typing import Protocol
from ..DomainLayer.User import User


class IAuthenticator(Protocol):

    def __init__(self, credentials): ...

    def authenticate(self) -> User: ...

    def get_auth(self): ...
