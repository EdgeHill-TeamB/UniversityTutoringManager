from abc import ABC, abstractmethod


class User(ABC):

    def is_authenticated(self) -> bool:
        return False
