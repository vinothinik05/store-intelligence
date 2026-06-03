from fastapi import FastAPI
from fastapi.responses import FileResponse
import csv

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Store Intelligence API Running"
    }


@app.get("/analytics")
def analytics():

    data = []

    with open("store_dashboard_report.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return {
        "analytics": data
    }


@app.get("/events")
def events():

    data = []

    with open("event_stream.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return {
        "events": data
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "Store Intelligence API"
    }


@app.get("/stores/STORE_001/metrics")
def store_metrics():

    return {
        "store_id": "STORE_001",
        "unique_visitors": 25,
        "conversion_rate": 12.5,
        "avg_dwell_time": 45,
        "queue_depth": 2,
        "abandonment_rate": 4.0
    }


@app.get("/stores/STORE_001/funnel")
def funnel():

    return {
        "store_id": "STORE_001",
        "entry": 25,
        "zone_visit": 20,
        "billing_queue": 15,
        "purchase": 10,
        "conversion_rate": 40.0
    }


@app.get("/stores/STORE_001/anomalies")
def anomalies():

    return {
        "store_id": "STORE_001",
        "anomalies": [
            {
                "type": "QUEUE_SPIKE",
                "severity": "WARN",
                "suggested_action": "Open another billing counter"
            },
            {
                "type": "CONVERSION_DROP",
                "severity": "INFO",
                "suggested_action": "Check product availability"
            }
        ]
    }


@app.get("/stores/STORE_001/heatmap")
def heatmap():

    return {
        "store_id": "STORE_001",
        "zones": [
            {
                "zone": "Entrance",
                "visit_frequency": 90,
                "avg_dwell": 12
            },
            {
                "zone": "Skincare",
                "visit_frequency": 75,
                "avg_dwell": 35
            },
            {
                "zone": "Billing",
                "visit_frequency": 60,
                "avg_dwell": 20
            }
        ],
        "data_confidence": "HIGH"
    }


@app.get("/dashboard")
def dashboard():

    return FileResponse("app/dashboard.html")