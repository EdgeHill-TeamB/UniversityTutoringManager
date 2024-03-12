from typing import Annotated, NamedTuple

from fastapi import Depends
from starlette.requests import Request as StarletteRequest


from api.core.Application.Authorisation.auth_service import TokenAuthorisationService
from api.core.Application.Authorisation.auth_response import AuthResponse
from api.Infrastructure.ExternalServices.Authorisation.jwt_authenticator import (
    JWTAuthenticator,
)
from api.Presentation.common._exceptions import (
    BadCredentialsException,
    RequiresAuthenticationException,
    PermissionDeniedException,
)


class AuthorizationHeaderElements(NamedTuple):
    authorization_scheme: str
    bearer_token: str
    are_valid: bool


def get_authorization_header_elements(
    authorization_header: str,
) -> AuthorizationHeaderElements:
    try:
        authorization_scheme, bearer_token = authorization_header.split()
    except ValueError:
        raise BadCredentialsException
    else:
        valid = authorization_scheme.lower() == "bearer" and bool(bearer_token.strip())
        return AuthorizationHeaderElements(authorization_scheme, bearer_token, valid)


def get_bearer_token(request: StarletteRequest) -> str:
    authorization_header = request.headers.get("Authorization")
    if authorization_header:
        authorization_header_elements = get_authorization_header_elements(
            authorization_header
        )
        if authorization_header_elements.are_valid:
            return authorization_header_elements.bearer_token
        else:
            raise BadCredentialsException
    else:
        raise RequiresAuthenticationException


def validate_token(token: Annotated[str, Depends()]) -> AuthResponse:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    token_validator = JWTAuthenticator(
        jwt_access_token="", auth0_issuer_url="", auth0_audience="", jwks_uri=""
    )
    return TokenAuthorisationService(token).get_credentials(
        token_validator=token_validator
    )


class PermissionsValidator:
    def __init__(self, required_permissions: list[str]):
        self.required_permissions = required_permissions

    def __call__(
        self, auth_credentials: Annotated[AuthResponse, Depends(validate_token)]
    ):
        token_permissions_set = set(auth_credentials.permissions)
        required_permissions_set = set(self.required_permissions)

        if not required_permissions_set.issubset(token_permissions_set):
            raise PermissionDeniedException
