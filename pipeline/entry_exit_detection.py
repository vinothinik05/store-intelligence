from ultralytics import YOLO
import cv2
import csv
from datetime import datetime

# Load YOLO Model
model = YOLO("yolov8n.pt")

# CAM 3 Video
cap = cv2.VideoCapture("dataset/CAM 3.mp4")

# Door Zone (adjust if needed)
door_x1 = 1050
door_y1 = 150

door_x2 = 1450
door_y2 = 720

previous_inside = {}

with open("entry_exit_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "visitor_id",
        "event_type"
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

        # Draw Door Zone
        cv2.rectangle(
            annotated,
            (door_x1, door_y1),
            (door_x2, door_y2),
            (0, 255, 255),
            3
        )

        cv2.putText(
            annotated,
            "DOOR ZONE",
            (door_x1, door_y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        if results[0].boxes.id is not None:

            ids = results[0].boxes.id.cpu().numpy().astype(int)
            boxes = results[0].boxes.xyxy.cpu().numpy()

            for box, track_id in zip(boxes, ids):

                x1, y1, x2, y2 = box

                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)

                cv2.circle(
                    annotated,
                    (center_x, center_y),
                    5,
                    (0, 0, 255),
                    -1
                )

                inside_zone = (
                    door_x1 <= center_x <= door_x2
                    and
                    door_y1 <= center_y <= door_y2
                )

                if track_id not in previous_inside:
                    previous_inside[track_id] = inside_zone

                else:

                    prev_state = previous_inside[track_id]

                    # ENTRY
                    if not prev_state and inside_zone:

                        print(f"ENTRY -> Visitor {track_id}")

                        writer.writerow([
                            datetime.now(),
                            track_id,
                            "ENTRY"
                        ])

                        file.flush()

                    # EXIT
                    elif prev_state and not inside_zone:

                        print(f"EXIT -> Visitor {track_id}")

                        writer.writerow([
                            datetime.now(),
                            track_id,
                            "EXIT"
                        ])

                        file.flush()

                    previous_inside[track_id] = inside_zone

        cv2.imshow(
            "Door Entry Exit Analytics",
            annotated
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

print("\n===========================")
print("ENTRY EXIT REPORT SAVED")
print("===========================")
print("File: entry_exit_report.csv")