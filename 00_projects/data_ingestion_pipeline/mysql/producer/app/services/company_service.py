from app.kafka.producer import KafkaProducer
from app.kafka.topics import COMPANY_CREATED
from app.utils import random_company_name, random_industry, random_country_id
from app.schemas.company import Company

class CompanyService:
    kafka: KafkaProducer

    def __init__(self):
        self.kafka = KafkaProducer()

    def generate_company(self):
        return Company(
            name=random_company_name(),
            industry=random_industry(),
            country_id=random_country_id()
        )

    def publish_company(self, company: Company):
        self.kafka.publish(
            topic = COMPANY_CREATED,
            key = "company",
            payload=company.model_dump()
        )

    def produce_companies(self, count: int):
        for _ in range(count):
            company = self.generate_company()
            self.kafka.publish(
                topic = COMPANY_CREATED,
                key = "company",
                payload=company.model_dump()
            )
        return count
