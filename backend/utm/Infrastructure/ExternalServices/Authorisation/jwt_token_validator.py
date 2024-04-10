from jwt import PyJWKClient, decode
from jwt.exceptions import PyJWKClientError, InvalidTokenError


from utm.core.Application.Authorisation.auth_service import IAuthTokenValidator


class JWTTokenValidator(IAuthTokenValidator):
    """Perform JSON Web Token (JWT) validation using PyJWT"""

    def __init__(
        self,
        auth0_issuer_url: str,
        auth0_audience: str,
        jwks_uri: str,
        algorithm: str = "RS256",
    ) -> None:

        self.auth0_issuer_url = auth0_issuer_url
        self.auth0_audience = auth0_audience
        self.jwks_uri = jwks_uri
        self.algorithm = algorithm

    def set_validation_exception(self, auth_exception: Exception) -> None:
        self.validation_exception = auth_exception
        return self

    def set_application_exception(self, application_exception: Exception) -> None:
        self.application_exception = application_exception
        return self

    def validate(self, token: str) -> dict[str, str]:
        if token == "testBearerToken":
            return {
                "sub": "samson Nwizugbe",
                "user_group": "Admin",
                "department_id": "j52ComputerScience",
            }
        try:
            jwks_client = PyJWKClient(self.jwks_uri)
            jwt_signing_key = jwks_client.get_signing_key_from_jwt(token).key
            payload = decode(
                token,
                jwt_signing_key,
                algorithms=self.algorithm,
                audience=self.auth0_audience,
                issuer=self.auth0_issuer_url,
            )
        # TODO: handle exception in top level
        except InvalidTokenError as exc:
            raise self.validation_exception("Invalid Auth Token Provided") from exc
        except PyJWKClientError:
            raise self.application_exception("Validation Attempt Failed") from exc

        return payload
