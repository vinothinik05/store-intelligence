# DESIGN.md

# Store Intelligence System Design

## Architecture Overview

The Store Intelligence system was designed as a modular pipeline that converts raw CCTV footage into actionable retail analytics.

The architecture consists of four major stages:

### 1. Detection Layer

The detection layer processes CCTV footage using YOLOv8 and OpenCV.

This layer is responsible for:

* Detecting people in video frames
* Tracking visitors across frames
* Counting unique visitors
* Detecting entry and exit events
* Generating structured behavioral events
* Producing analytics such as loitering and heatmaps

The output of this layer is a stream of structured events stored in CSV format.

Example events:

* ENTRY
* EXIT
* VISITOR_DETECTED

These events act as the foundation for downstream analytics.

---

### 2. Event Stream Layer

All detected visitor actions are converted into structured records and stored in event_stream.csv.

Each event contains:

* Timestamp
* Visitor ID
* Event Type
* Zone Information

This event stream serves as the ingestion source for the Intelligence API.

The design allows future migration from CSV files to message brokers such as Kafka or RabbitMQ without major architectural changes.

---

### 3. Intelligence API Layer

The Intelligence API is implemented using FastAPI.

The API exposes store intelligence through REST endpoints.

Key endpoints include:

* /health
* /events
* /analytics
* /dashboard
* /stores/STORE_001/metrics
* /stores/STORE_001/funnel
* /stores/STORE_001/heatmap
* /stores/STORE_001/anomalies

The API reads event data and computes store-level insights.

The design separates detection logic from business intelligence logic, making the system easier to maintain and scale.

---

### 4. Dashboard Layer

The dashboard provides a simple visualization layer for store metrics.

It displays:

* Visitor counts
* Conversion metrics
* Funnel information
* Heatmap statistics
* Operational anomalies

The dashboard consumes data directly from the API, ensuring a clean separation between presentation and analytics layers.

---

# System Flow

CCTV Video

↓

YOLOv8 Detection & Tracking

↓

Event Generation

↓

event_stream.csv

↓

FastAPI Intelligence Service

↓

Dashboard & Analytics

---

# Scalability Considerations

The current implementation uses CSV files for simplicity and rapid development.

For production deployment, the following improvements can be made:

* PostgreSQL for persistent storage
* Kafka for event streaming
* Redis for caching analytics
* Kubernetes for deployment scaling
* Multi-camera synchronization

The architecture was intentionally designed so these upgrades can be added without redesigning the entire system.

---

# AI-Assisted Decisions

AI tools were actively used during the development process.

### Decision 1: Detection Model Selection

Several detection models were considered, including YOLOv8 and MediaPipe.

AI-assisted comparisons suggested YOLOv8 due to its balance between speed, accuracy, and ease of integration.

After testing, YOLOv8 was selected because it provided reliable person detection while maintaining real-time performance.

### Decision 2: Event Stream Design

AI suggested multiple schema approaches.

The final design adopted a simple event-based architecture using structured CSV files because it allowed quick validation and easy debugging.

This approach also keeps the pipeline modular and future-ready for migration to Kafka.

### Decision 3: API Architecture

AI proposed combining analytics directly inside the detection pipeline.

This approach was rejected.

Instead, a separate FastAPI service was implemented.

Separating analytics from detection improved maintainability, reduced coupling, and more closely matched production system design patterns.

In all cases, AI suggestions were reviewed, modified, and validated before integration into the final implementation.
