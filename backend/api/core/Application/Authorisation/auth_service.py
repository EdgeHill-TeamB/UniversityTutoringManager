from .auth_response import AuthResponse

from typing import Protocol


class IAuthTokenValidator(Protocol):

    def validate(self) -> dict[str, str]: ...


class IAuthorisationService(Protocol):

    def create_validation_token(
        self,
    ) -> AuthResponse: ...


class TokenAuthorisationService(IAuthorisationService):

    def __init__(self, token: str) -> None:
        self.token = token

    def get_credentials(self, token_validator: IAuthTokenValidator) -> AuthResponse:
        """_summary_

        Args:
            email (str): _description_
            password_hash (str): _description_

        Returns:
            AuthResponse: _description_
        """
        creds = token_validator.validate(self.token)

        return AuthResponse(
            "test_first_name", "test_last_name", "test_email@test.com", "test_token"
        )
