from app.kafka.producer import KafkaProducer
from app.kafka.topics import COUNTRIES_CREATED
from app.utils import COUNTRIES

class CountryService:
    kafka: KafkaProducer

    def __init__(self):
        self.kafka = KafkaProducer()

    def publish_country(self, payload):
        self.kafka.publish(
            topic = COUNTRIES_CREATED,
            key = "countries",
            payload=payload
        )

    def produce_countries(self):
        for country in COUNTRIES:
            self.kafka.publish(
                topic = COUNTRIES_CREATED,
                key = "countries",
                payload=country
            )
        return len(COUNTRIES)
