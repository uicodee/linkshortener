from fastapi import FastAPI

from .authentication import router as authentication_router
from .link import router as short_router


def setup(app: FastAPI) -> None:
    app.include_router(
        router=authentication_router,
        tags=["authentication"]
    )
    app.include_router(
        router=short_router,
        tags=["short"]
    )

