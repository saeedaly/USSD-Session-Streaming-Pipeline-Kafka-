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
- JSON-based payloads for easy downstream integration
- Simple local Kafka testing setup using Docker

## Tech Stack

- Python 3.8+
- Confluent Kafka
- Apache Kafka
- Docker

## Prerequisites

Before starting, make sure you have:

- Python 3.8 or newer
- Docker installed and running

## Installation

1. Clone the repository.
2. Install the Kafka client:
   ```bash
   pip install confluent-kafka
   ```
3. Start Kafka locally with Docker:
   ```bash
   docker compose up -d
   ```

## Usage

Start the consumer first:

```bash
python consumer.py
```

Then start the producer in a second terminal:

```bash
python producer.py
```

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

