from app.api.middleware import UserSessionMiddleware
from app.api.routers import parcels
from fastapi import FastAPI


def get_app():
    app = FastAPI()
    app.include_router(parcels.router, tags=["parcels"])
    app.add_middleware(UserSessionMiddleware)
    return app