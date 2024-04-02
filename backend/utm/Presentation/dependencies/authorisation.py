from typing import Annotated, NamedTuple
from fastapi import Depends
from starlette.requests import Request as StarletteRequest
from utm.core.Application.Authorisation.auth_service import TokenAuthorisationService
from utm.core.Application.Common.authorised_user import AuthorisedUser
from utm.core.Application.Common._exceptions import ErrorTypes
from utm.Infrastructure.ExternalServices.Authorisation.jwt_authenticator import (
    JWTTokenValidator,
)
from ..common._exceptions import (
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


def validate_token(token: Annotated[str, Depends(get_bearer_token)]) -> dict[str, str]:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    token_validator = JWTTokenValidator(
        jwt_access_token="", auth0_issuer_url="", auth0_audience="", jwks_uri=""
    )
    result = TokenAuthorisationService(
        token, token_validator=token_validator
    ).get_credentials()

    if result:
        return result.value
    else:
        raise PermissionDeniedException(
            error_type=ErrorTypes.PERMISSION_ERROR,
            message="You do not have permission to view this resource",
        )


def get_request_user(
    creds: Annotated[AuthorisedUser, Depends(validate_token)]
) -> AuthorisedUser:
    return AuthorisedUser(
        user_id=creds["user_id"],
        user_group=creds["user_group"],
        department_id=creds["department_id"],
    )
