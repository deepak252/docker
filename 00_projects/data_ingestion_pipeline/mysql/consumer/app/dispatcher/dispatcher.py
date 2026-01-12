from app.consumer.topics import COUNTRY_CREATED, MCHANNEL_CREATED, COMPANY_CREATED, PRODUCT_CREATED, PRODUCT_MEDIA_CREATED
from app.writers.country_writer import CountryWriter
from app.writers.media_channel_writer import MediaChannelWriter
from app.writers.company_writer import CompanyWriter
from app.writers.product_writer import ProductWriter
from app.writers.product_media_writer import ProductMediaWriter
from app.utils.logger import get_logger

logger = get_logger(__name__)


class Dispatcher:
    def __init__(self):
        self.mapping = {
            COUNTRY_CREATED: CountryWriter(),
            MCHANNEL_CREATED: MediaChannelWriter(),
            COMPANY_CREATED: CompanyWriter(),
            PRODUCT_CREATED: ProductWriter(),
            PRODUCT_MEDIA_CREATED: ProductMediaWriter(),
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
        