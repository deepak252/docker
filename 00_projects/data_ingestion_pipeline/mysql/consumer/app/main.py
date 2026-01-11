from app.core.config import settings
from app.core.kafka import KafkaClient
from app.consumer.kafka_consumer import KafkaConsumer
from app.dispatcher.dispatcher import Dispatcher
from app.sinks.runner import SinkRunner
from app.core.topics import COUNTRIES_CREATED
from app.utils.logger import setup_logging, get_logger

logger = get_logger(__name__)

def main():
    setup_logging()
    logger.info("🚀 Starting Kafka ingestion service")
    consumer = KafkaClient.get_consumer(
        group_id=settings.KAFKA_CONSUMER_GROUP
    )

    dispatcher = Dispatcher()
    sink_runner = SinkRunner()

    kafka_consumer = KafkaConsumer(
        consumer=consumer,
        dispatcher=dispatcher,
        sink_runner=sink_runner
    )

    kafka_consumer.start(
        topics=[
            COUNTRIES_CREATED,
        ]
    )

if __name__ == "__main__":
    main()
