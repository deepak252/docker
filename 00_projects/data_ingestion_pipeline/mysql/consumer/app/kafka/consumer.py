# from app.kafka.client import Retr
from confluent_kafka import Consumer
import json

class KafkaConsumer:
    def __init__(self, consumer: Consumer, dispatcher):
        self.consumer = consumer
        self.dispatcher = dispatcher
        # self.retry = RetryPublisher()

    def start(self, topics: list[str]):
        self.consumer.subscribe(topics)

        while True:
            msg = self.consumer.poll(1.0)

            if not msg or msg.error():
                continue

            payload = json.loads(msg.value())

            try:
                self.dispatcher.dispatch(msg.topic(), payload)
                self.consumer.commit(msg)

            except Exception as e:
                print(e)
                # self.retry.handle(msg, payload, e)
