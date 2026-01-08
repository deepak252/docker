from app.kafka.producer import KafkaProducer
from app.kafka.topics import COUNTRIES_CREATED
from app.utils import COUNTRIES
from app.schemas.country import Country

class CountryService:
    kafka: KafkaProducer

    def __init__(self):
        self.kafka = KafkaProducer()

    def publish_country(self, country: Country):
        self.kafka.publish(
            topic = COUNTRIES_CREATED,
            key = "countries",
            payload=country.model_dump()
        )

    def produce_countries(self):
        for country in COUNTRIES:
            country = Country(
                name = country[0],
                iso_code = country[1]
            )
            self.kafka.publish(
                topic = COUNTRIES_CREATED,
                key = "countries",
                payload=country.model_dump()
            )
        return len(COUNTRIES)
