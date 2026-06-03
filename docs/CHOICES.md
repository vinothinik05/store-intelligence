# CHOICES.md

# Key Technical Decisions

## Decision 1: Detection Model Selection

### Options Considered

1. YOLOv8
2. RT-DETR
3. MediaPipe
4. Faster R-CNN

### AI Suggestion

AI tools recommended YOLOv8 and RT-DETR because both provide strong object detection performance for retail analytics applications.

RT-DETR offered slightly better accuracy but required additional setup and higher computational resources.

### Final Choice

YOLOv8

### Why YOLOv8 Was Chosen

YOLOv8 was selected because:

* Easy integration
* Fast inference speed
* Strong person detection accuracy
* Built-in tracking support
* Large community support
* Suitable for real-time deployment

The challenge focused on delivering a complete pipeline quickly and reliably. YOLOv8 provided the best balance between speed and implementation effort.

---

## Decision 2: Event Schema Design

### Options Considered

1. Complex JSON Event Schema
2. CSV-based Event Stream
3. Hybrid JSON + Database Storage

### AI Suggestion

AI tools recommended using a detailed JSON schema with metadata, confidence scores and session tracking information.

### Final Choice

CSV Event Stream with Structured Fields

### Why This Choice Was Made

The challenge required structured events that could be consumed by the analytics layer.

The selected schema contains:

* Timestamp
* Visitor ID
* Event Type
* Zone

Benefits:

* Easy debugging
* Human-readable format
* Lightweight storage
* Fast integration with FastAPI

The design remains flexible and can later be upgraded to a full event streaming platform such as Kafka.

---

## Decision 3: API Architecture

### Options Considered

1. FastAPI Monolith
2. Microservices Architecture
3. Serverless Functions

### AI Suggestion

AI-generated recommendations proposed a microservices architecture because it scales well across multiple stores.

### Final Choice

FastAPI Monolith

### Why This Choice Was Made

For the challenge scope, a monolithic FastAPI application provided several advantages:

* Faster development
* Simpler deployment
* Easier debugging
* Lower operational complexity

All analytics endpoints remain within a single service.

Implemented endpoints include:

* /health
* /events
* /analytics
* /dashboard
* /stores/STORE_001/metrics
* /stores/STORE_001/funnel
* /stores/STORE_001/heatmap
* /stores/STORE_001/anomalies

---

## AI Feedback That Was Overridden

AI tools suggested implementing:

* Kafka event streaming
* PostgreSQL storage
* Multi-service architecture

These ideas were useful but considered excessive for the challenge timeline.

Instead, a simpler architecture was chosen that could still demonstrate:

* Detection
* Tracking
* Event generation
* Analytics computation
* Dashboard visualization

while remaining easy to run using Docker Compose.

---

## Lessons Learned

During development, AI tools accelerated:

* Code generation
* API development
* Docker configuration
* Event schema design
* Analytics endpoint creation

However, final architectural decisions were made manually after evaluating complexity, implementation time and challenge requirements.

The result is a practical end-to-end retail analytics platform that balances functionality, maintainability and deployment simplicity.
