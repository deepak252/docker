from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer(
        "topic1", 
        bootstrap_servers= 'localhost:9092', 
        auto_offset_reset = 'earliest', 
        group_id = 'consumer-group-c')
    
    print("Starting the Consumser")
    for msg in consumer:
        print("User: {}".format(json.loads(msg.value)))

        

