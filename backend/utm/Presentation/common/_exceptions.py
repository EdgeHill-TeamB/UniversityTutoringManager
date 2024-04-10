from fastapi import HTTPException, status
from utm.core.Application.Common._exceptions import ErrorTypes


class InternalServerErrorException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


class BadCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Bad credentials"
        )


class PermissionDeniedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied"
        )


class RequiresAuthenticationException(HTTPException):
    def __init__(self, detail: str = "Requires authentication"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class UnableToVerifyException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to verify credentials",
        )


class ResourceNotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


ERRORS = {
    ErrorTypes.RESOURCE_ERROR: ResourceNotFoundException,
    ErrorTypes.AUTHORISATION_ERROR: RequiresAuthenticationException,
}
