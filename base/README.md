# USSD-Session-Streaming-Pipeline-Kafka-Base
A lightweight Apache Kafka project that simulates real-time USSD session events — the way telecom networks handle short codes like #7115# — using a Python producer and consumer built with confluent-kafka.

# 🧠 Overview
The project consists of two independent microservices:

producer.py — Simulates a telecom network generating USSD dial sessions (random MSISDNs, service codes, and delivery statuses) and publishes them as JSON events to a Kafka topic every 2 seconds.
consumer.py — Subscribes to the topic, consumes the session events, and prints them in real time.

# ✨ Features
🎲 Realistic event simulation — random Egyptian MSISDNs (2012XXXXXXXX), real-style USSD service codes, and weighted delivery statuses.
⚖️ Weighted statuses — SUCCESS (92%), FAILED (6%), TIMEOUT (2%)
🔁 Consumer group support with earliest offset reset for replayability
🧾 JSON message format for easy integration with downstream systems

# 🛠️ Tech Stack
Python
confluent-kafka	Kafka producer & consumer client
Apache Kafka	Event streaming platform
Docker	Running Kafka locally

# 📋 Prerequisites
Python 3.8+
A running Kafka broker on localhost:9092

# ⚙️ Installation
1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.gitcd <your-repo-name>
2. pip install confluent-kafka
3. docker compose up -d
# 🚀 Usage
Terminal 1 — start the consumer first:
  python consumer.py
Terminal 2 — start the producer:
  python producer.py
Press Ctrl + C in either terminal to stop gracefully (the producer flushes pending messages; the consumer closes cleanly).

# 🖥️ Sample Output
Producer:

✅ Session sent{"session_id":"20127654321020250101143012","dial":"201276543210","timestamp":"2025-01-01 14:30:12.34","service_code":"#7115#","status": "SUCCESS"}

Consumer:

🟢 4 Received session: 20127654321020250101143012 from 201276543210 and it was SUCCESS

