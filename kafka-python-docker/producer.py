from kafka import KafkaProducer
import json
from data import get_random_user
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers= ['localhost:9092'], value_serializer=json_serializer)


if __name__ == '__main__':
    while 1==1:
        user = get_random_user()
        producer.send("topic1", user)
        print(user)
        time.sleep(5)
        

