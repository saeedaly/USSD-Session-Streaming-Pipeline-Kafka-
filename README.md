# USSD-Session-Streaming-Pipeline-Kafka-
A lightweight Apache Kafka project that simulates real-time USSD session events — the way telecom networks handle short codes like #7115# — using a Python producer and consumer built with confluent-kafka.

# 🧠 Overview
The project consists of two independent microservices:

producer.py — Simulates a telecom network generating USSD dial sessions (random MSISDNs, service codes, and delivery statuses) and publishes them as JSON events to a Kafka topic every 2 seconds.
consumer.py — Subscribes to the topic, consumes the session events, and prints them in real time.

# ✨ Features
🎲 Realistic event simulation — random Egyptian MSISDNs (2012XXXXXXXX), real-style USSD service codes, and weighted delivery statuses
⚖️ Weighted statuses — SUCCESS (92%), FAILED (6%), TIMEOUT (2%)
📨 Async production with delivery report callbacks (topic / partition / offset confirmation)
🔁 Consumer group support with earliest offset reset for replayability
🧾 JSON message format for easy integration with downstream systems

# 🛠️ Tech Stack
Tool	Purpose
Python 3	Core language
confluent-kafka	Kafka producer & consumer client
Apache Kafka	Event streaming platform
Docker (optional)	Running Kafka locally
# 📋 Prerequisites
Python 3.8+
A running Kafka broker on localhost:9092
pip package manager
# ⚙️ Installation
1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.gitcd <your-repo-name>
2. Install Python dependencies
pip install confluent-kafka
3. Start Kafka locally (Docker)
The easiest way is a single-node KRaft Kafka container:

# docker-compose.ymlservices:  kafka:    image: apache/kafka:latest    container_name: kafka    ports:      - "9092:9092"    environment:      KAFKA_NODE_ID: 1      KAFKA_PROCESS_ROLES: broker,controller      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@localhost:9093      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
docker compose up -d
4. (Optional) Create the topic manually
Kafka auto-creates topics by default, but you can create it explicitly:

docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \  --create --topic ussd-sessions \  --bootstrap-server localhost:9092 \  --partitions 3 --replication-factor 1
# 🚀 Usage
Terminal 1 — start the consumer first:

python consumer.py
Terminal 2 — start the producer:

python producer.py
Press Ctrl + C in either terminal to stop gracefully (the producer flushes pending messages; the consumer closes cleanly).

# 🖥️ Sample Output
Producer:

✅ Session sent {"session_id": "20127654321020250101143012", "dial": "201276543210", "timestamp": "2025-01-01 14:30:12.34", "service_code": "#7115#", "status": "SUCCESS"}✅ Session sent to: ussd-sessions > partition 0 > at offset 42
Consumer:

🟢 Consumer is running and subscribed to ussd-sessions topic✅ 0 Received session: 20127654321020250101143012 from 201276543210 and it was SUCCESS
# 📨 Event Schema
Each message published to the ussd-sessions topic is a JSON object:

Field	Type	Description	Example
session_id	string	Unique ID (dial + timestamp)	20127654321020250101143012
dial	string	Simulated MSISDN (phone number)	201276543210
timestamp	string	Session creation time	2025-01-01 14:30:12.34
service_code	string	USSD short code dialed	#7115#
status	string	Session outcome	SUCCESS | FAILED | TIMEOUT
Example payload:

{  "session_id": "20127654321020250101143012",  "dial": "201276543210",  "timestamp": "2025-01-01 14:30:12.34",  "service_code": "#7115#",  "status": "SUCCESS"}
🔧 Configuration
Setting	File	Default	Description
bootstrap.servers	both	localhost:9092	Kafka broker address
group.id	consumer.py	ussd-sessions	Consumer group ID
auto.offset.reset	consumer.py	earliest	Read from the beginning when no offset exists
Topic	both	ussd-sessions	Target Kafka topic
Publish interval	producer.py	2 seconds	Delay between generated events
Service codes	producer.py	#012#, #7115#, #75#, #704#	Simulated USSD codes
