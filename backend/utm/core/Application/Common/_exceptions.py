class ErrorTypes:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"


class UTMApplicationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.error_type = ErrorTypes.SYSTEM_ERROR


class UTMInternalApplicationFailure(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.error_type = ErrorTypes.SYSTEM_ERROR


class UTMValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.error_type = ErrorTypes.PARAMETERS_ERROR
