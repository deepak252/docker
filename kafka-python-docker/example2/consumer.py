from confluent_kafka import Consumer
# https://www.confluent.io/blog/configuring-apache-kafka-consumer-group-ids/

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "group2",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["example2.topic1"])


print("Listening...")

while True:
    msg = consumer.poll(timeout=1.0)
    if msg is None:
        continue
    if msg.error():
        print("Error:", msg.error())
        continue

    print(f"Received: {msg.value().decode()} from partition {msg.partition()}")
    