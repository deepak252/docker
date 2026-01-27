from fastapi import APIRouter
from app.routes import search, health

api_router = APIRouter()
api_router.include_router(search.router)
api_router.include_router(health.router)
