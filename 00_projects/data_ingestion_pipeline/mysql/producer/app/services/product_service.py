from app.kafka.producer import KafkaProducer
from app.kafka.topics import PRODUCT_CREATED
from app.schemas.product import Product
from app.utils import random_country_id, random_mchannel_id, random_date_recent, random_category, random_sentence, random_date
import random


class ProductService:
    def __init__(self):
        self.kafka = KafkaProducer()

    def generate_product(self) -> Product:
        start_date = random_date_recent(days=1800)
        end_date = random_date(start_date)
        budget = random.randint(1000, 100000)
        return Product(
            company_id=random.randint(1, 4500),
            media_channel_id=random_mchannel_id(),
            country_id=random_country_id(),
            title=random_sentence(3),    
            description=random_sentence(50),  
            category=random_category(),
            start_date=start_date,
            end_date=end_date,
            budget=budget,
        )

    def publish_product(self, product: Product):
        self.kafka.publish(
            topic=PRODUCT_CREATED,
            key="product",
            payload=product.model_dump()
        )

    def produce_products(self, count: int) -> int:
        for _ in range(count):
            product = self.generate_product()
            self.publish_product(product)
        return count
