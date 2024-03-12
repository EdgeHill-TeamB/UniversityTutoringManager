import jwt
from jwt.exceptions import PyJWKClientError, InvalidTokenError


from api.core.Application.Authorisation.auth_service import IAuthTokenValidator


class JWTAuthenticator(IAuthTokenValidator):
    """Perform JSON Web Token (JWT) validation using PyJWT"""

    def __init__(
        self,
        jwt_access_token: str,
        auth0_issuer_url: str,
        auth0_audience: str,
        jwks_uri: str,
        algorithm: str = "RS256",
    ) -> None:

        self.jwt_access_token = jwt_access_token
        self.auth0_issuer_url = auth0_issuer_url
        self.auth0_audience = auth0_audience
        self.algorithm = algorithm
        self.jwks_uri = jwks_uri

    def validate(self):
        try:
            jwks_client = jwt.PyJWKClient(self.jwks_uri)
            jwt_signing_key = jwks_client.get_signing_key_from_jwt(
                self.jwt_access_token
            ).key
            payload = jwt.decode(
                self.jwt_access_token,
                jwt_signing_key,
                algorithms=self.algorithm,
                audience=self.auth0_audience,
                issuer=self.auth0_issuer_url,
            )
        # TODO: handle exception in top level
        except (PyJWKClientError, InvalidTokenError) as exc:
            return exc
        return payload
