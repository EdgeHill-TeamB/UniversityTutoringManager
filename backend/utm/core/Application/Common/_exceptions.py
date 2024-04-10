class ErrorTypes:
    AUTHORISATION_ERROR = "AuthorisationError"
    PERMISSION_ERROR = "PermissionError"
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"


class UTMApplicationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.error_type = ErrorTypes.SYSTEM_ERROR


class UTMInternalApplicationFailure(UTMApplicationError):
    def __init__(self, message):
        super().__init__(message)
        self.error_type = ErrorTypes.SYSTEM_ERROR


class UTMValidationError(UTMApplicationError):
    def __init__(self, message):
        super().__init__(message)
        self.error_type = ErrorTypes.AUTHORISATION_ERROR
