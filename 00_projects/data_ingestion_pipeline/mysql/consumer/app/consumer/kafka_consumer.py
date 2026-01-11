from confluent_kafka import Consumer
from app.dispatcher.dispatcher import Dispatcher
from app.sinks.runner import SinkRunner
from app.utils.logger import get_logger
import json

logger = get_logger(__name__)

class KafkaConsumer:
    def __init__(self, consumer: Consumer, dispatcher: Dispatcher, sink_runner: SinkRunner):
        self.consumer = consumer
        self.dispatcher = dispatcher
        self.sink_runner = sink_runner
        # self.retry = RetryPublisher()

    def start(self, topics: list[str]):
        self.consumer.subscribe(topics)
        logger.info("✅ Subscribed to kafka topics")

        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue
            
            topic = msg.topic()

            if msg.error():
                logger.error(
                    "Kafka error | topic=%s | error=%s",
                    topic,
                    msg.error()
                )
                continue

            if not msg or msg.error():
                continue

            payload = json.loads(msg.value())

            try:
                logger.info(
                    "Received message | topic=%s | offset=%s",
                    topic,
                    msg.offset()
                )
                # self.dispatcher.dispatch(msg.topic(), payload)
                writer = self.dispatcher.get_writer(msg.topic())
                self.sink_runner.run(writer, [payload])
                self.consumer.commit(msg)

                logger.info(
                    "Processed message | topic=%s | offset=%s",
                    topic,
                    msg.offset()
                )

            except Exception as e:
                logger.exception(
                    "Failed processing message | topic=%s | offset=%s",
                    topic,
                    msg.offset()
                )
                # self.retry.handle(msg, payload, e)

