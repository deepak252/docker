from confluent_kafka import Producer
from app.core.config import settings

class KafkaClient:
    _producer: Producer | None = None

    @classmethod
    def get_producer(cls):
        if not cls._producer:
            cls._producer = Producer({
                "bootstrap.servers": settings.KAFKA_BOOTSTRAP,
                "acks": "all",
                "retries": 5,
                "enable.idempotence": True,
                "linger.ms": 20,
            })
        return cls._producer

def delivery_report(err, msg):
    if err:
        print("delivery failed:", err)
    else:
        print(f"Delivered {msg.topic()} [{msg.partition()}] offset={msg.offset()}")