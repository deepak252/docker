from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err:
        print("Delivery failed:", err)
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


for i in range(1, 6):
    producer.produce(
        "example2.topic1",
        key=str(i),
        value=f"Hello Kafka {i}",
        callback=delivery_report
    )

producer.flush()