from typing import Any, Coroutine, Awaitable, Callable
from fastapi import Request, Response
import secure
from starlette.middleware.base import BaseHTTPMiddleware

secure_headers = secure.Secure(
    csp=secure.ContentSecurityPolicy().default_src("'self'").frame_ancestors("'none'"),
    hsts=secure.StrictTransportSecurity().max_age(31536000).include_subdomains(),
    referrer=secure.ReferrerPolicy().no_referrer(),
    cache=secure.CacheControl().no_cache().no_store().max_age(0).must_revalidate(),
    xfo=secure.XFrameOptions().deny(),
)


class SecureHeaders(BaseHTTPMiddleware):
    def __init__(self, app) -> None:
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Coroutine[Any, Any, Response]:
        response = await call_next(request)
        secure_headers.framework.fastapi(response)
        return response
