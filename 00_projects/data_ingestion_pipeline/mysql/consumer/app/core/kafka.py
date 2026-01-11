from confluent_kafka import Producer, Consumer
from app.core.config import settings

def delivery_report(err, msg):
    if err:
        print("delivery failed:", err)
    else:
        print(f"Delivered {msg.topic()} [{msg.partition()}] offset={msg.offset()}")
        
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
    
    @classmethod
    def get_consumer(cls, group_id: str):
        return Consumer({
            "bootstrap.servers": settings.KAFKA_BOOTSTRAP,
            "group.id": group_id,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False
        })