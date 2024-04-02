from abc import ABC, abstractmethod


class ResponseTypes:
    PERMISSION_ERROR = "PermissionError"
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


class Result(ABC):

    def __init__(self) -> None:
        self.type = None
        self.value = None

    @abstractmethod
    def __bool__(self) -> bool: ...


class SuccessResult(Result):

    def __init__(self, _value):
        super().__init__()
        self.type = ResponseTypes.SUCCESS
        self.value = _value

    def __bool__(self) -> bool:
        return True


class FailureResult(Result):

    def __init__(self, type_, message):
        super().__init__()
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return f"{msg.__class__.__name__} : {str(msg)}"
        return msg

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self) -> bool:
        return True
