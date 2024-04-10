from utm.core.Application.Authorisation.auth_service import IAuthTokenValidator


class MemTokenValidator(IAuthTokenValidator):
    """Perform JSON Web Token (JWT) validation using PyJWT"""

    def __init__(self) -> None:
        self._exceptions = {
            "testBearerTokenInvalid": None,
            "testBearerTokenApplicationError": None,
        }

    def set_validation_exception(
        self, auth_exception: Exception
    ) -> "MemTokenValidator":
        self.validation_exception = auth_exception
        self._exceptions["testBearerTokenInvalid"] = self.validation_exception(
            "Invalid Auth Token Provided"
        )
        return self

    def set_application_exception(
        self, application_exception: Exception
    ) -> "MemTokenValidator":
        self.application_exception = application_exception
        self._exceptions["testBearerTokenApplicationError"] = (
            self.application_exception("Validation Attempt Failed")
        )
        return self

    def validate(self, token: str) -> dict[str, str]:
        if token == "testBearerToken":
            return {
                "sub": "samson6398@gmail.com",
                "user_group": "Admin",
                "department_id": "Computer Science",
            }
        else:
            raise self._exceptions.get(
                token, self.validation_exception("Invalid Auth Token Provided")
            )
