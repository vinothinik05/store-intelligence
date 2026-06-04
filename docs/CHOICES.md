# CHOICES.md

# Engineering Decisions

This document explains the major engineering decisions made during the development of the Store Intelligence system.

---

# Decision 1: Detection Model Selection

## Options Considered

1. YOLOv8
2. MediaPipe
3. Haar Cascade
4. Traditional OpenCV Detection

## AI Suggestion

AI-assisted evaluation suggested YOLOv8 because it provides a strong balance between detection accuracy, tracking compatibility, inference speed, and ease of deployment.

MediaPipe was more suitable for pose estimation tasks than retail visitor analytics.

Traditional OpenCV approaches were lightweight but struggled under varying lighting conditions and crowded scenes.

## Final Choice

YOLOv8

## Why It Was Chosen

YOLOv8 was selected because it offers:

* High person detection accuracy
* Fast inference performance
* Easy integration with tracking pipelines
* Real-time CCTV processing capability
* Strong community support

The challenge requires customer detection, visitor counting, tracking, and event generation. YOLOv8 provided the most practical balance between performance and implementation complexity.

## Trade-Offs

Advantages:

* High accuracy
* Real-time performance
* Easy deployment
* Reliable retail analytics

Disadvantages:

* Requires GPU for optimal speed
* Occlusions can affect tracking accuracy

Despite these limitations, YOLOv8 was the best choice for the challenge timeline and requirements.

---

# Decision 2: Event Schema Design

## Options Considered

1. Simple CSV Event Schema
2. JSON Event Schema
3. Database-First Schema
4. Kafka Style Event Streaming Schema

## AI Suggestion

AI recommended building the system around structured events instead of storing only aggregated metrics.

The suggestion was based on event-driven architecture principles where detection, analytics, and visualization remain independent components.

## Final Choice

Structured CSV Event Stream

Schema:

```text
timestamp,visitor_id,event_type,zone
```

Example:

```text
2026-06-03 11:29:45,1,VISITOR_DETECTED,Store Area
2026-06-03 11:30:12,3,ENTRY,Main Door
2026-06-03 11:31:05,3,EXIT,Main Door
```

## Why It Was Chosen

The detection layer and intelligence layer were intentionally separated through an event stream.

Each field serves a specific purpose:

### timestamp

Used for:

* Traffic analysis
* Visitor trends
* Time-based analytics
* Event ordering

### visitor_id

Used for:

* Unique visitor counting
* Session tracking
* Analytics calculations

### event_type

Represents visitor actions:

* ENTRY
* EXIT
* VISITOR_DETECTED

This enables funnel and visitor flow analysis.

### zone

Identifies where the event occurred.

Examples:

* Main Door
* Store Area
* Billing Area

This enables future heatmap and zone analytics.

## Analytics Supported By This Schema

The schema allows the API to calculate:

* Total visitors
* Unique visitors
* Visitor flow
* Entry counts
* Exit counts
* Zone statistics
* Traffic analytics
* Dashboard metrics

## Alternative Designs Considered

### JSON Schema

Example:

```json
{
  "event_id": "uuid",
  "store_id": "STORE_001",
  "camera_id": "CAM_2",
  "visitor_id": "VIS_001",
  "event_type": "ENTRY",
  "timestamp": "2026-06-03T11:29:45Z",
  "zone": "Main Door",
  "confidence": 0.92
}
```

This approach is more production-ready but increases implementation complexity.

### Database-First Design

Events would be written directly into a relational database.

This was rejected because it added setup complexity and slowed development.

## Future Improvements

For a production deployment the schema would be extended with:

* event_id
* store_id
* camera_id
* confidence
* dwell_time
* is_staff
* session_id
* metadata

These fields would support:

* Cross-camera tracking
* Staff exclusion
* Re-entry detection
* Confidence-based analytics
* Advanced behavioral analysis

The current schema was chosen because it satisfies challenge requirements while remaining simple, transparent, and easy to validate.

---

# Decision 3: API Architecture Choice

## Options Considered

1. Flask
2. FastAPI
3. Django REST Framework
4. Analytics Without API Layer

## AI Suggestion

AI suggested FastAPI because of:

* Automatic API documentation
* Strong typing support
* Excellent performance
* Modern architecture
* Minimal boilerplate

## Final Choice

FastAPI

## Why It Was Chosen

The challenge requires a queryable intelligence layer.

FastAPI enabled rapid implementation of:

* Health endpoint
* Events endpoint
* Analytics endpoint
* Metrics endpoint
* Funnel endpoint
* Heatmap endpoint
* Anomaly endpoint
* Dashboard integration

Automatic Swagger documentation available at:

```text
/docs
```

was also a significant advantage.

## Trade-Offs

Advantages:

* High performance
* Excellent developer experience
* Automatic documentation
* Easy Docker deployment
* Production-friendly structure

Disadvantages:

* Smaller ecosystem than Django
* Requires additional infrastructure for very large deployments

For the challenge scope, FastAPI provided the fastest path to a complete and maintainable solution.

---

# Conclusion

The final Store Intelligence architecture combines:

* YOLOv8 for customer detection and tracking
* Structured event streams for analytics ingestion
* FastAPI for intelligence APIs and dashboard integration

AI tools were used to evaluate alternatives, compare design trade-offs, generate initial implementation ideas, and accelerate development.

However, all final decisions were reviewed against project requirements and validated through implementation and testing before being adopted in the final system.
