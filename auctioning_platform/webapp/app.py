from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from webapp import api


def create_app() -> FastAPI:
    """Create web server."""

    app = FastAPI(title="Auctions", version="0.1.0")


    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api.router)

    return app
