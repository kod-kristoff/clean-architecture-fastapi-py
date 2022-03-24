from fastapi import status
from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
async def test_health_check_works(client: AsyncClient):
    response = await client.get("/health_check")

    assert response.status_code == status.HTTP_200_OK
