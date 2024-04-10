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
        # super().__init__()
        self.type_ = ResponseTypes.SUCCESS
        self._value = _value

    @property
    def type(self):
        return self.type_

    @property
    def value(self):
        return self._value

    def __bool__(self) -> bool:
        return True


class FailureResult(Result):

    def __init__(self, type_, message):
        # super().__init__()
        self.type_ = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return msg.args[0]
        return msg

    @property
    def type(self):
        return self.type_

    @property
    def value(self):
        return self.message

    def __bool__(self) -> bool:
        return False
