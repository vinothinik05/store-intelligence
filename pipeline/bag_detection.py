from ultralytics import YOLO
import cv2
import time
import csv
import os

# ==========================
# LOAD MODEL
# ==========================
model = YOLO("yolov8x.pt")

# ==========================
# VIDEO
# ==========================
cap = cv2.VideoCapture("dataset/CAM 4.mp4")

# ==========================
# SETTINGS
# ==========================
CONFIDENCE = 0.20
ABANDONED_TIME = 30

os.makedirs("alerts", exist_ok=True)

TARGET_CLASSES = [
    "backpack",
    "handbag",
    "suitcase"
]

bag_times = {}
alerted = set()
report_data = []

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, conf=CONFIDENCE)

    annotated = frame.copy()

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])
            class_name = model.names[cls]

            if class_name not in TARGET_CLASSES:
                continue

            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # Track ID based on position
            bag_id = f"{center_x//30}_{center_y//30}"

            if bag_id not in bag_times:
                bag_times[bag_id] = time.time()

            stay_time = (
                time.time()
                - bag_times[bag_id]
            )

            color = (255, 0, 0)

            if stay_time > ABANDONED_TIME:
                color = (0, 0, 255)

            # Draw box
            cv2.rectangle(
                annotated,
                (x1, y1),
                (x2, y2),
                color,
                3
            )

            # Class name
            cv2.putText(
                annotated,
                f"{class_name} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

            # Timer
            cv2.putText(
                annotated,
                f"{stay_time:.1f}s",
                (x1, y2 + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            # Alert
            if (
                stay_time > ABANDONED_TIME
                and bag_id not in alerted
            ):

                print(
                    f"ABANDONED BAG ALERT: {bag_id}"
                )

                alerted.add(bag_id)

                report_data.append([
                    bag_id,
                    round(stay_time, 2),
                    class_name,
                    "ABANDONED"
                ])

                # Save screenshot
                filename = (
                    f"alerts/{bag_id}.jpg"
                )

                cv2.imwrite(
                    filename,
                    annotated
                )

                cv2.putText(
                    annotated,
                    "ABANDONED BAG ALERT!",
                    (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

    cv2.imshow(
        "Bag Detection - CAM 4",
        annotated
    )

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

# ==========================
# SAVE CSV REPORT
# ==========================
with open(
    "bag_report.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Bag ID",
        "Time Seen",
        "Bag Type",
        "Status"
    ])

    writer.writerows(report_data)

print("=" * 50)
print("Bag Report Saved")
print("Total Alerts:", len(report_data))
print("=" * 50)

cap.release()
cv2.destroyAllWindows()