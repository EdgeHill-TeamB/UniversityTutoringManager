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
    heartbeat_router = APIRouter()

    @heartbeat_router.get("/heartbeat")
    async def posts():
        return {"heartbeat": "active"}

    from utm.Presentation.routes.Admin import router as admin_router
    from utm.Presentation.routes.PersonalTutor import router as personal_tutor_router
    from utm.Presentation.routes.Student import router as student_router
    from utm.Presentation.routes.StudentCohort import router as student_cohort_router
    from utm.Presentation.routes.Meeting import router as meeting_router

    app.include_router(heartbeat_router, prefix="/test")
    app.include_router(router=admin_router, prefix="/admin")
    app.include_router(router=personal_tutor_router, prefix="/personal-tutor")
    app.include_router(router=student_router, prefix="/student")
    app.include_router(router=student_cohort_router, prefix="/student-cohort")
    app.include_router(router=meeting_router, prefix="/meeting")

    return app
