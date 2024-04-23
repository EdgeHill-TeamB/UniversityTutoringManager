from ..Common.authorised_user import AuthorisedUser
from ..Common.responses import Result, SuccessResult, FailureResult
from ..Common._exceptions import UTMApplicationError


from typing import Protocol


class IAuthTokenValidator(Protocol):

    def validate(self, token: str) -> dict[str, str]: ...


class IAuthorisationService(Protocol):

    def create_validation_token(
        self,
    ) -> AuthorisedUser: ...


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
            response = {
                "user_id": creds["sub"],
                "user_group": creds["user_group"],
                "department_id": creds["department_id"],
            }

            result = SuccessResult(_value=response)

        except UTMApplicationError as exc:
            result = FailureResult(type_=exc.error_type, message=exc)

        return result
