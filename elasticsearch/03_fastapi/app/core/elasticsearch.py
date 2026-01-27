import logging
from elasticsearch import AsyncElasticsearch
from app.core.config import settings

logger = logging.getLogger(__name__)

es_client: AsyncElasticsearch | None = None


async def connect_elasticsearch():
    global es_client
    try:
        es_client = AsyncElasticsearch(
            hosts=[settings.ELASTICSEARCH_HOST],
            basic_auth=(
                settings.ELASTICSEARCH_USERNAME,
                settings.ELASTICSEARCH_PASSWORD,
            ) if settings.ELASTICSEARCH_USERNAME else None,
            request_timeout=30,
            retry_on_timeout=True,
            max_retries=3,
        )
        await es_client.info()
        logger.info("Connected to Elasticsearch")
    except Exception:
        logger.exception("Failed to connect to Elasticsearch")
        raise


async def close_elasticsearch():
    if es_client:
        await es_client.close()
        logger.info("Elasticsearch connection closed")


async def get_es_client() -> AsyncElasticsearch:
    return es_client
