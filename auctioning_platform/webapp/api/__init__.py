from fastapi import APIRouter

from webapp.api import health_check


router = APIRouter()


router.include_router(health_check.router)
