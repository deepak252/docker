from app.core.elasticsearch import get_es_client

PRODUCT_INDEX = "products"

PRODUCT_MAPPING = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "product_id": {"type": "long"},
            "name": {
                "type": "text",
                "fields": {
                    "keyword": {"type": "keyword"}
                }
            },
            "category": {"type": "keyword"},
            "price": {"type": "float"},
            "in_stock": {"type": "boolean"},
            "created_at": {"type": "date"}
        }
    }
}


async def create_product_index():
    es = await get_es_client()
    exists = await es.indices.exists(index=PRODUCT_INDEX)
    if not exists:
        await es.indices.create(
            index=PRODUCT_INDEX,
            body=PRODUCT_MAPPING
        )
