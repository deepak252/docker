# app/kafka/dispatcher.py
from app.kafka.topics import COUNTRIES_CREATED
from app.handlers.countries import CountryHandler

class Dispatcher:
    def __init__(self):
        self.handlers = {
            COUNTRIES_CREATED: CountryHandler(),
            # PRODUCTS: ProductHandler(),
        }

    def dispatch(self, topic: str, payload: dict):
        handler = self.handlers.get(topic)

        if not handler:
            raise Exception(f"No handler for topic {topic}")

        handler.handle(payload)
