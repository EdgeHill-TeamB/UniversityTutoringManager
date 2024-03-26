from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def create_app() -> FastAPI:

    app = FastAPI()

    app = inject_middlewares(app, {})

    app = inject_routers(app)

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request, exc):
        message = str(exc.detail)

        return JSONResponse({"message": message}, status_code=exc.status_code)

    return app


def inject_middlewares(app: FastAPI, config: dict[str, str]) -> FastAPI:

    from utm.Presentation.middlewares.secure_headers import SecureHeaders

    app.add_middleware(SecureHeaders)

    from fastapi.middleware.cors import CORSMiddleware

    # allow_origins=[config["client_origin_url"]],
    app.add_middleware(
        CORSMiddleware,
        allow_methods=["GET"],
        allow_headers=["Authorization", "Content-Type"],
        max_age=86400,
    )

    return app


def inject_routers(app: FastAPI) -> FastAPI:
    test_router = APIRouter()

    @test_router.get("/heartbeat")
    async def posts():
        return {"heartbeat": "active"}

    app.include_router(test_router, prefix="/test")

    # http://localhost:8080/personal-tutor/user-details

    return app
