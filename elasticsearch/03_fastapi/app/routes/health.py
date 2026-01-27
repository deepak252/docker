from fastapi import APIRouter
from app.core.elasticsearch import get_es_client

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/elasticsearch")
async def elasticsearch_health():
    es = await get_es_client()
    return await es.cluster.health()
