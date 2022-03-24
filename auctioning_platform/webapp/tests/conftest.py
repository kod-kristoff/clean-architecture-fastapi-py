import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient


@pytest.fixture
def app() -> FastAPI:
    """Create a new application for testing"""
    from webapp.app import create_app
    return  create_app()


@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncClient:
    """Make requests in our tests"""
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            # headers={"Content-Type": "application/json"}
        ) as client:
            yield client
