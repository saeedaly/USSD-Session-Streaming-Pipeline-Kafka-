from confluent_kafka import Producer
from datetime import datetime, timezone
import time
import uuid
import json
import random


SERVICE_CODES = ["#012#", "#7115#", "#75#","#704#"]
STATUSES = ["SUCCESS", "FAILED", "TIMEOUT"]
STATUS_WEIGHTS = [0.92, 0.06, 0.02]

def random_msisdn():
    return "2012" + f"{random.randint(0, 99999999):08d}"

producer_config ={
    'bootstrap.servers': 'localhost:9092'
    }

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"❌ Failed to sent session due to: {err}")
    else:
        print(f"✅ Session sent {msg.value().decode('utf-8')}")
        print(f"✅ Session sent to: {msg.topic()} > partition {msg.partition()} > at offset {msg.offset()}")

try:
    while True:
        dial = random_msisdn()
        timestamp = datetime.now()
        event = {
            "session_id": dial + timestamp.strftime("%Y%m%d%H%M%S"),
            "dial": dial,
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4],
            "service_code": random.choice(SERVICE_CODES),
            "status": random.choices(STATUSES, weights=STATUS_WEIGHTS, k=1)[0],
            }

        value = json.dumps(event).encode("utf-8")

        producer.produce(topic="ussd-sessions", value=value, callback=delivery_report)
        producer.poll(0)
        time.sleep(2)

except KeyboardInterrupt:
    print("\n Stopping Producer")        
finally:
    producer.flush()