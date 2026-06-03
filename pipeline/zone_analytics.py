from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open CAM 2 video
cap = cv2.VideoCapture("dataset/CAM 2.mp4")

# Save current zone of each person
person_zones = {}

while True:

    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    # Divide screen into 3 zones
    zone1 = w // 3
    zone2 = (w * 2) // 3

    # Detect + Track
    results = model.track(frame, persist=True, classes=[0])

    # Draw detections
    annotated = results[0].plot()

    # Draw zone lines
    cv2.line(annotated, (zone1, 0), (zone1, h), (0, 255, 0), 2)
    cv2.line(annotated, (zone2, 0), (zone2, h), (0, 255, 0), 2)

    # Zone labels
    cv2.putText(annotated, "ZONE A", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(annotated, "ZONE B", (zone1 + 50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(annotated, "ZONE C", (zone2 + 50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # Check persons
    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()

        for box, track_id in zip(boxes, ids):

            x1, y1, x2, y2 = box

            center_x = int((x1 + x2) / 2)

            # Find zone
            if center_x < zone1:
                zone = "ZONE_A"

            elif center_x < zone2:
                zone = "ZONE_B"

            else:
                zone = "ZONE_C"

            person_id = int(track_id)

            # First time
            if person_id not in person_zones:

                person_zones[person_id] = zone

                print(f"NEW PERSON {person_id} IN {zone}")

            # Zone changed
            else:

                old_zone = person_zones[person_id]

                if old_zone != zone:

                    print(
                        f"EVENT: PERSON {person_id} MOVED FROM {old_zone} TO {zone}"
                    )

                    person_zones[person_id] = zone

    cv2.imshow("Zone Analytics", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()