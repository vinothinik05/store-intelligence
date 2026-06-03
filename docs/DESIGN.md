# DESIGN.md

# Store Intelligence System - Architecture Design

## Overview

The Store Intelligence System is designed to transform raw CCTV footage into actionable retail analytics. The architecture follows a pipeline-based approach where video feeds are processed, visitor events are generated, analytics are computed, and results are exposed through REST APIs and a live dashboard.

The system consists of four major layers:

1. Detection Layer
2. Event Stream Layer
3. Intelligence API Layer
4. Dashboard Layer

---

## Detection Layer

The detection layer is responsible for processing CCTV footage and identifying visitors inside the store.

YOLOv8 was selected as the primary detection model because it provides a strong balance between speed and accuracy. The model detects people from CCTV frames and assigns tracking IDs using the built-in tracking functionality.

The system performs:

* Person detection
* Visitor tracking
* Customer counting
* Entry monitoring
* Exit monitoring
* Zone monitoring

Each detected visitor receives a unique tracking identifier which acts as a session token during processing.

---

## Event Stream Layer

The event stream layer converts detections into structured events.

Generated events are written into CSV-based event streams.

Example event types include:

* VISITOR_DETECTED
* ENTRY
* EXIT

Each event contains:

* Timestamp
* Visitor ID
* Event Type
* Zone Information

The event stream acts as the bridge between the computer vision layer and the analytics API.

---

## Intelligence API Layer

The Intelligence API is implemented using FastAPI.

The API exposes analytics endpoints that provide real-time information about store activity.

Implemented endpoints include:

* /
* /health
* /events
* /analytics
* /dashboard
* /stores/STORE_001/metrics
* /stores/STORE_001/funnel
* /stores/STORE_001/heatmap
* /stores/STORE_001/anomalies

The API is containerized using Docker and can be started through docker compose.

---

## Dashboard Layer

The dashboard layer provides a simple visualization interface for store metrics.

The dashboard fetches analytics information from API endpoints and displays store activity in a browser.

Metrics displayed include:

* Total Visitors
* Analytics Reports
* Event Stream Data
* Conversion Metrics
* Heatmap Data

---

# AI-Assisted Decisions

Artificial Intelligence tools were used extensively during development.

## Decision 1: Detection Model Selection

AI tools suggested multiple detection approaches including YOLOv8, RT-DETR and MediaPipe.

After comparing complexity and implementation speed, YOLOv8 was selected because it provides reliable person detection and integrated tracking support.

## Decision 2: Event Schema Design

AI-assisted brainstorming helped define a simple event schema containing timestamps, visitor identifiers and event types.

The final design was simplified to ensure compatibility with FastAPI endpoints and dashboard reporting.

## Decision 3: API Architecture

Several API architectures were considered.

AI tools suggested a microservice-based architecture. However, a single FastAPI service was selected because it reduced complexity and was sufficient for the challenge requirements.

---

## Deployment Strategy

The entire application is deployed through Docker Compose.

Deployment includes:

* FastAPI Service
* Dashboard
* Event Processing Components

Running the following command starts the complete system:

docker compose up --build

This approach ensures reproducibility and simplifies evaluation on a clean machine.

---

## Future Improvements

Future enhancements may include:

* Cross-camera visitor re-identification
* Staff identification
* Real-time event streaming using Kafka
* PostgreSQL-based storage
* Advanced anomaly detection
* Live WebSocket dashboards
* Multi-store support

---

## Conclusion

The Store Intelligence System demonstrates a complete end-to-end retail analytics pipeline. It processes CCTV footage, generates visitor events, computes analytics, exposes APIs, and visualizes results through a dashboard while remaining easy to deploy using Docker.
