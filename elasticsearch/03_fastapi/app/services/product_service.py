import logging
from app.core.elasticsearch import get_es_client
from app.indices.product_index import PRODUCT_INDEX

logger = logging.getLogger(__name__)


class ProductService:

    @staticmethod
    async def index_product(product: dict):
        logger.info("Indexing product", extra={"product_id": product.get("product_id")})
        es = await get_es_client()
        await es.index(index=PRODUCT_INDEX, document=product)

    @staticmethod
    async def search_products(query: str):
        es = await get_es_client()
        response = await es.search(
            index=PRODUCT_INDEX,
            body={
                "query": {
                    "match": {
                        "name": query
                    }
                }
            }
        )
        return response["hits"]["hits"]
