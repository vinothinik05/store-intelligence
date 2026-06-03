from ultralytics import YOLO
import cv2
import csv
from datetime import datetime

# Load YOLO Model
model = YOLO("yolov8n.pt")

# Video Path
cap = cv2.VideoCapture("dataset/CAM 2.mp4")

# Store IDs
seen_ids = set()

# Event Stream CSV
with open("event_stream.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "visitor_id",
        "event_type",
        "zone"
    ])

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model.track(
            frame,
            persist=True,
            classes=[0]
        )

        annotated = results[0].plot()

        current_customers = 0

        if results[0].boxes.id is not None:

            ids = results[0].boxes.id.cpu().numpy().astype(int)

            current_customers = len(ids)

            for track_id in ids:

                if track_id not in seen_ids:

                    seen_ids.add(track_id)

                    writer.writerow([
                        datetime.now(),
                        track_id,
                        "VISITOR_DETECTED",
                        "Store Area"
                    ])

                    file.flush()

        total_visitors = len(seen_ids)

        cv2.putText(
            annotated,
            f"Current Customers: {current_customers}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            annotated,
            f"Total Visitors: {total_visitors}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.imshow(
            "Customer Counting Analytics",
            annotated
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

print("\n================================")
print("CUSTOMER COUNTING REPORT")
print("================================")
print("Total Unique Visitors :", len(seen_ids))
print("Event Stream Saved : event_stream.csv")
print("================================")