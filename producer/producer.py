from kafka import KafkaProducer
import json
import time
import random
import os

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def random_order():
    return {
        "action": random.choice(["buy", "sell"]),
        "stock": "HAHN",
        "quantity": random.randint(1, 10),
        "timestamp": time.time()
    }

while True:
    order = random_order()
    producer.send('stock_orders', order)
    print(f"Produced: {order}")
    time.sleep(0.5)
