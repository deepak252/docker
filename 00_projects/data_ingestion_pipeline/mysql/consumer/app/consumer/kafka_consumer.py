from confluent_kafka import Consumer
from app.dispatcher.dispatcher import Dispatcher
from app.sinks.runner import SinkRunner
from app.utils.logger import get_logger
import json
import time

logger = get_logger(__name__)

BATCH_SIZE = 1000
POLL_TIMEOUT = 1.0
FLUSH_INTERVAL = 5  # seconds
MAX_RETRIES = 5

class KafkaConsumer:
    def __init__(self, consumer: Consumer, dispatcher: Dispatcher, sink_runner: SinkRunner):
        self.consumer = consumer
        self.dispatcher = dispatcher
        self.sink_runner = sink_runner
        self.buffer = []
        self.last_flush_time = time.time()
        self.retry_count = 0
        # self.retry = RetryPublisher()

    def start(self, topics: list[str]):
        self.consumer.subscribe(topics)
        logger.info("✅ Subscribed to kafka topics: %s", topics)

        while True:
            msgs = self.consumer.consume(
                num_messages=BATCH_SIZE,
                timeout=POLL_TIMEOUT
            )

            if not msgs:
                self._flush_if_needed()
                continue

            for msg in msgs:
                if msg is None:
                    continue

                if msg.error():
                    logger.error(
                        "Kafka error | topic=%s | error=%s",
                        msg.topic(),
                        msg.error()
                    )
                    continue

                payload = json.loads(msg.value())
                self.buffer.append((msg, payload))

            if len(self.buffer) >= BATCH_SIZE:
                self._flush()


    def _flush_if_needed(self):
        if (
            self.buffer
            and time.time() - self.last_flush_time >= FLUSH_INTERVAL
        ):
            self._flush()

    def _flush(self):
        logger.info("Flushing batch | size=%d", len(self.buffer))

        try:
            records_by_writer = {}

            # group payloads by topic/writer
            for msg, payload in self.buffer:
                writer = self.dispatcher.get_writer(msg.topic())
                records_by_writer.setdefault(writer, []).append(payload)

            # write to sinks
            for writer, records in records_by_writer.items():
                self.sink_runner.run(writer, records)

            # commit offsets AFTER successful DB write
            self.consumer.commit(asynchronous=False)

            logger.info(
                "Batch processed successfully | count=%d",
                len(self.buffer)
            )

            self.buffer.clear()
            self.last_flush_time = time.time()

        except Exception:
            # DO NOT COMMIT → Kafka will retry
            self.retry_count += 1

            logger.exception(
                "❌ Batch processing failed | retry=%d/%d",
                self.retry_count,
                MAX_RETRIES
            )

            if self.retry_count >= MAX_RETRIES:
                self._handle_permanent_failure()
    
    def _handle_permanent_failure(self):
        logger.error(
            "🚨 Batch permanently failed after %d retries | committing offsets",
            MAX_RETRIES
        )

        # Option 1 Send to DLQ (recommended)
        # self.retry.publish_batch(self.buffer)

        # Option 2 Skip & commit (last resort)
        # self.consumer.commit(asynchronous=False)

        # Option 3 Stop consumer (strict)
        # raise RuntimeError("Stopping consumer due to repeated failures")

        self.consumer.commit(asynchronous=False)  # REQUIRED

        self.buffer.clear()
        self.retry_count = 0
        self.last_flush_time = time.time()

    # def start(self, topics: list[str]):
    #     self.consumer.subscribe(topics)
    #     logger.info("✅ Subscribed to kafka topics")

    #     while True:
    #         msg = self.consumer.poll(1.0)

    #         if msg is None:
    #             continue
            
    #         topic = msg.topic()

    #         if msg.error():
    #             logger.error(
    #                 "Kafka error | topic=%s | error=%s",
    #                 topic,
    #                 msg.error()
    #             )
    #             continue

    #         if not msg or msg.error():
    #             continue

    #         payload = json.loads(msg.value())

    #         try:
    #             logger.info(
    #                 "Received message | topic=%s | offset=%s",
    #                 topic,
    #                 msg.offset()
    #             )
    #             # self.dispatcher.dispatch(msg.topic(), payload)
    #             writer = self.dispatcher.get_writer(msg.topic())
    #             self.sink_runner.run(writer, [payload])
    #             self.consumer.commit(msg)

    #             logger.info(
    #                 "Processed message | topic=%s | offset=%s",
    #                 topic,
    #                 msg.offset()
    #             )

    #         except Exception as e:
    #             logger.exception(
    #                 "Failed processing message | topic=%s | offset=%s",
    #                 topic,
    #                 msg.offset()
    #             )
    #             # self.retry.handle(msg, payload, e)

