from kafka import KafkaConsumer
import json
import time
import random
import os

consumer = KafkaConsumer(
    'stock_orders',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='stock-dashboard'
)

price = 100.0
data = []

shared_path = "/shared/price_data.json"
os.makedirs("/shared", exist_ok=True)

for message in consumer:
    order = message.value
    action = order.get("action")
    timestamp = time.time()

    if action == "buy":
        price += round(random.uniform(0.1, 1.0), 2)
    elif action == "sell":
        price -= round(random.uniform(0.1, 1.0), 2)

    data.append({"timestamp": timestamp, "price": price})

    with open(shared_path, "w") as f:
        json.dump(data[-20:], f)
