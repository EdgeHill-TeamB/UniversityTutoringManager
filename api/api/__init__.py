from fastapi import FastAPI, APIRouter


def create_app() -> FastAPI:

    test_router = APIRouter()

    app = FastAPI()  # FastAPI(lifespan=lifespan)

    @test_router.get("/heartbeat")
    async def posts():
        return {"heartbeat": "active"}

    app = inject_routers(app)

    return app


def inject_routers(app: FastAPI) -> FastAPI:
    from api.PresentationLayer.Authentication import router as authentication_router

    app.include_router(authentication_router)

    return app
