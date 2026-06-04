# Store Intelligence Challenge

## Overview

This project implements a complete retail store intelligence pipeline that processes CCTV footage, generates visitor events, exposes analytics through a FastAPI service, and displays live store metrics through a dashboard.

Pipeline Flow:

Raw CCTV Clips → Detection Layer → Event Stream → Intelligence API → Dashboard

---

## Features

### Detection Layer

* YOLOv8 person detection
* Multi-object tracking
* Visitor counting
* Entry and Exit detection using door camera
* Event generation
* Visitor session tracking
* Heatmap analytics
* Loitering detection
* Zone analytics

### Event Stream

Generated events are stored in:

```text
event_stream.csv
```

Supported events:

* ENTRY
* EXIT
* VISITOR_DETECTED

### Intelligence API

Built using FastAPI.

Available endpoints:

```text
/
/health
/events
/analytics
/dashboard
/stores/STORE_001/metrics
/stores/STORE_001/funnel
/stores/STORE_001/heatmap
/stores/STORE_001/anomalies
```

### Dashboard

Provides live store analytics including:

* Visitor count
* Conversion metrics
* Zone statistics
* Heatmap information
* Operational anomalies

---

## Project Structure

```text
store-intelligence/

├── app/
│   ├── main.py
│   └── dashboard.html
│
├── docs/
│   ├── DESIGN.md
│   └── CHOICES.md
│
├── dataset/
│   ├── CAM 1.mp4
│   ├── CAM 2.mp4
│   ├── CAM 3.mp4
│   ├── CAM 4.mp4
│   └── CAM 5.mp4
│
├── pipeline/
│   ├── detect.py
│   ├── customer_counting.py
│   ├── entry_exit_detection.py
│   ├── heatmap_analytics.py
│   ├── loitering_detection.py
│   ├── zone_analytics.py
│   └── bag_detection.py
│
├── event_stream.csv
├── store_dashboard_report.csv
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone <repository-url>
cd store-intelligence
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Detection Pipeline

### Customer Analytics

```bash
python pipeline/customer_counting.py
```

### Entry Exit Analytics

```bash
python pipeline/entry_exit_detection.py
```

### Heatmap Analytics

```bash
python pipeline/heatmap_analytics.py
```

### Zone Analytics

```bash
python pipeline/zone_analytics.py
```

### Loitering Detection

```bash
python pipeline/loitering_detection.py
```

### Abandoned Object Detection

```bash
python pipeline/bag_detection.py
```

Generated outputs:

```text
event_stream.csv
entry_exit_report.csv
store_dashboard_report.csv
loitering_report.csv
bag_report.csv
```

---

## Running API

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Open API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Docker Deployment

Run using Docker:

```bash
docker compose up --build
```

Open:

```text
http://127.0.0.1:8000/docs
```

Dashboard:

```text
http://127.0.0.1:8000/dashboard
```

---

## Health Check

```text
GET /health
```

Returns service status and API health information.

---

## Metrics Endpoint

```text
GET /stores/STORE_001/metrics
```

Returns:

* Unique visitors
* Conversion rate
* Average dwell time
* Queue depth
* Abandonment rate

---

## Funnel Endpoint

```text
GET /stores/STORE_001/funnel
```

Returns visitor conversion funnel:

* Entry
* Zone Visit
* Billing Queue
* Purchase

---

## Heatmap Endpoint

```text
GET /stores/STORE_001/heatmap
```

Returns zone-wise visit frequency and dwell statistics.

---

## Anomalies Endpoint

```text
GET /stores/STORE_001/anomalies
```

Returns active store anomalies and operational alerts.

---

## Dashboard

Open:

```text
http://127.0.0.1:8000/dashboard
```

Displays live store analytics and intelligence metrics.

---

## Technologies Used

* Python
* YOLOv8
* OpenCV
* FastAPI
* Docker
* HTML Dashboard

---

## Author

Vinothini Kanthasamy

Store Intelligence Challenge Submission
