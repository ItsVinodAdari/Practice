"""
This is a Kafka Consumer basic code to receive data from
Kafka Producer
"""
from kafka import KafkaConsumer

consumer = KafkaConsumer('first_topic',
                         bootstrap_servers=['localhost:9092'])
try:
    for message in consumer:
        if message.value == b"quit":
            print("Message Transfer Completed")
            exit()
        print(message)
except KeyboardInterrupt:
    exit()

