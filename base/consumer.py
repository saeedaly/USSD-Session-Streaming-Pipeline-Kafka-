from confluent_kafka import Consumer
import json

consumer_config={
    "bootstrap.servers": "localhost:9092",
    "group.id": "ussd-sessions",
    "auto.offset.reset": "earliest" 
}

consumer = Consumer(consumer_config)

consumer.subscribe(["ussd-sessions"])

print("🟢 Consusmer is running and subscribed to ussd-sessions topic")

try:
    while True:
        msg=consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error", msg.error())
            continue
        value = msg.value().decode("utf-8")
        event = json.loads(value)
        print(f"✅ {msg.offset()} Received session: {event['session_id']} from {event['dial']} and it was {event['status']}")

except KeyboardInterrupt:
    print("\n Stopping Consumer")

finally:
    consumer.close()


