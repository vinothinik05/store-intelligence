<<<<<<< HEAD
# Store Intelligence System

## Overview

This project is a retail analytics platform that processes CCTV footage, detects visitors, tracks movement, generates structured events, exposes analytics APIs, and displays live dashboard metrics.

---

## Features

* Person Detection using YOLOv8
* Visitor Tracking
* Entry / Exit Detection
* Event Stream Generation
* Real-time Analytics API
* Anomaly Detection
* Heatmap Analytics
* Conversion Funnel Analytics
* Dockerized Deployment
* Live Dashboard

---

## Project Structure

store-intelligence/

* pipeline/
* app/
* event_stream.csv
* store_dashboard_report.csv
* Dockerfile
* docker-compose.yml
* README.md

---

## Run Project

### Build and Start

docker compose up --build

### Open API

http://localhost:8000/docs

### Dashboard

http://localhost:8000/dashboard

### Analytics

http://localhost:8000/analytics

---

## Detection Pipeline

The detection pipeline uses YOLOv8 to detect and track visitors from CCTV footage.

Generated output:

* Visitor Detection Events
* Entry Events
* Exit Events
* Event Stream CSV

---

## API Endpoints

* /
* /health
* /analytics
* /events
* /dashboard
* /stores/STORE_001/metrics
* /stores/STORE_001/funnel
* /stores/STORE_001/heatmap
* /stores/STORE_001/anomalies

---

## Docker Deployment

docker compose up --build

Starts:

* FastAPI Application
* Analytics Dashboard
* Event APIs

---

## Author

Vinothini Kandhasamy
=======
# store-intelligence
>>>>>>> fc85c675e62b746f2be5b7613c74d3d8d66fe10a
