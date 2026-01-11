from app.kafka.client import KafkaClient, delivery_report
import json

class KafkaProducer:

    def publish(self, topic: str, key: str, payload: dict):

        producer = KafkaClient.get_producer()

        producer.produce(
            topic=topic,
            key=key, # The key decides to which partition the message goes, and ensures ordering per key
            value=json.dumps(payload, default=str),
            callback=delivery_report,
        )

        producer.flush()
