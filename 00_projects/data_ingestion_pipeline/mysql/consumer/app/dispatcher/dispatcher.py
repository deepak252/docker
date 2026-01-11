from app.consumer.topics import COUNTRIES_CREATED
from app.writers.country_writer import CountryWriter
from app.utils.logger import get_logger

logger = get_logger(__name__)


class Dispatcher:
    def __init__(self):
        self.mapping = {
            COUNTRIES_CREATED: CountryWriter(),
            # PRODUCTS: ProductHandler(),
        }
    def get_writer(self, topic: str):
        writer = self.mapping.get(topic)

        if not writer:
            logger.error("No writer registered for topic=%s", topic)
            raise Exception(f"No writer registered for topic {topic}")
        return writer
    # def dispatch(self, topic: str, payload: dict):
    #     writer = self.mapping.get(topic)

    #     if not writer:
    #         raise Exception(f"No writer for topic {topic}")
    #     if writer is MySQLWritable:
    #         MySQLSink().write([payload], writer)
    #     if writer is ElasticWritable:
    #         ElasticSink().write([payload], writer)
        