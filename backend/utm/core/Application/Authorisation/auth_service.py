from .auth_response import AuthResponse
from ..Common.responses import Result, SuccessResult, FailureResult
from ..Common._exceptions import UTMApplicationError


from typing import Protocol


class IAuthTokenValidator(Protocol):

    def validate(self) -> dict[str, str]: ...


class IAuthorisationService(Protocol):

    def create_validation_token(
        self,
    ) -> AuthResponse: ...


class TokenAuthorisationService(IAuthorisationService):

    def __init__(self, token: str, token_validator: IAuthTokenValidator) -> None:
        self.token = token
        self.token_validator = token_validator

    def get_credentials(
        self,
    ) -> Result:
        """_summary_

        Args:
            email (str): _description_
            password_hash (str): _description_

        Returns:
            AuthResponse: _description_
        """
        result = None
        try:
            creds = self.token_validator.validate(self.token)
            auth_response = AuthResponse(
                first_name=creds.a,
                last_name=creds.b,
                email=creds.c,
                credentials=creds.d,
            )
            result = SuccessResult(_value=auth_response)
        except UTMApplicationError as exc:
            result = FailureResult(type_=exc.error_type, message=exc)

        return result
