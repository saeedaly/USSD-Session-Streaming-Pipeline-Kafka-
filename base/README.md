# USSD Session Streaming Pipeline - Base

A lightweight Apache Kafka project that simulates real-time USSD session events using a Python producer and consumer. It mimics telecom systems that generate session activity such as USSD dial attempts, service-code requests, and delivery outcomes.

## Overview

This project contains two independent microservices:

- `producer.py`: generates realistic USSD session events and publishes them to a Kafka topic
- `consumer.py`: consumes those events and prints them in real time

The producer simulates a telecom network producing events like:
- mobile numbers
- service codes such as `#7115#`
- timestamps
- delivery status (`SUCCESS`, `FAILED`, `TIMEOUT`)

## Features

- Realistic event simulation using Egyptian MSISDN examples
- Real-style USSD service codes
- Weighted status handling:
  - `SUCCESS`: 92%
  - `FAILED`: 6%
  - `TIMEOUT`: 2%
- Consumer group support with offset reset for replayability
- JSON-based payloads for easy downstream integration
- Simple local Kafka testing setup using Docker

## Tech Stack

- Python 3.8+
- Confluent Kafka Python client
- Apache Kafka
- Docker

## Prerequisites

Before starting, make sure you have:

- Python 3.8 or newer
- Docker installed and running
- A Kafka broker available at `localhost:9092`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Install the Kafka client:
   ```bash
   pip install confluent-kafka
   ```

3. Start Kafka locally with Docker:
   ```bash
   docker compose up -d
   ```

4. Confirm Kafka is reachable:
   ```bash
   kafka-topics --bootstrap-server localhost:9092 --list
   ```

## Configuration

Make sure your producer and consumer use the same Kafka topic. For example:

```python
TOPIC = "ussd-events"
```

If your project uses a different topic name, update both files to match.

## Usage

Start the consumer first:

```bash
python consumer.py
```

Then start the producer in a second terminal:

```bash
python producer.py
```

To stop the services, press `Ctrl + C`. The producer flushes any pending messages before exiting.

## Example Output

### Producer
```json
{"session_id":"20127654321020250101143012","dial":"201276543210","timestamp":"2025-01-01 14:30:12.34","service_code":"#7115#","status":"SUCCESS"}
```

### Consumer
```text
🟢 4 Received session: 20127654321020250101143012 from 201276543210 and it was SUCCESS
```

## Project Structure

```text
.
├── producer.py
├── consumer.py
├── docker-compose.yml
├── README.md
└── requirements.txt
```

## Troubleshooting

### Kafka connection errors
- Ensure Docker is running
- Verify Kafka is listening on `localhost:9092`
- Check the container logs:
  ```bash
  docker compose logs -f
  ```

### No messages received
- Confirm both producer and consumer use the same topic name
- Start the consumer before the producer
- Check whether the consumer group reset is configured correctly

## License

This project is intended for learning and demonstration purposes.
