from kafka import KafkaConsumer
from pprint import pprint

if __name__ == '__main__':
    consumer = KafkaConsumer('helloKafka', bootstrap_servers="localhost:9092",
                             enable_auto_commit=False, auto_offset_reset="earliest")
    pprint(consumer.metrics())
    for msg in consumer:
        pprint(msg)