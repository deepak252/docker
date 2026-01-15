from app.kafka.producer import KafkaProducer
from app.kafka.topics import PRODUCT_MEDIA_CREATED
from app.schemas.product_media import ProductMedia
from app.utils import (
    random_media_type,
    random_media_url,
)
import random

class ProductMediaService:
    def __init__(self):
        self.kafka = KafkaProducer()

    def generate_product_media(self, product_id = random.randint(1, 4000)) -> ProductMedia:
        media_type = random_media_type()
        return ProductMedia(
            product_id=product_id,  # product_id (FK-safe range)
            media_type=media_type,
            media_url=random_media_url(media_type)
        )
    
    def publish_product_media(self, media: ProductMedia):
        self.kafka.publish(
            topic=PRODUCT_MEDIA_CREATED,
            key="product_media",
            payload=media.model_dump()
        )

    # def produce_product_media(self, count: int) -> int:
        # for _ in range(count):
        #     media = self.generate_product_media()
        #     self.publish_product_media(media)
        # return count
    def produce_product_media(self, start_id: int, end_id: int) -> int:
        if start_id > end_id:
            raise ValueError("start_id must be <= end_id")

        produced = 0

        for product_id in range(start_id, end_id + 1):
            media = self.generate_product_media(product_id)
            self.publish_product_media(media)
            produced += 1

        return produced
