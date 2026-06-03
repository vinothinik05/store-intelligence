from ultralytics import YOLO
import cv2
import time
import csv

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture("dataset/CAM 5.mp4")

# ==========================
# COUNTER AREA (CAM 5)
# ==========================
COUNTER_X1 = 500
COUNTER_Y1 = 150

COUNTER_X2 = 1280
COUNTER_Y2 = 1080

# Store entry times
entry_time = {}

# Alert only once
alerted = set()

# Report data
report_data = []

while True:

    ret, frame = cap.read()

    if not ret:
        print("Video Finished")
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0]
    )

    annotated = results[0].plot()

    # Draw Counter Area
    cv2.rectangle(
        annotated,
        (COUNTER_X1, COUNTER_Y1),
        (COUNTER_X2, COUNTER_Y2),
        (0, 255, 0),
        3
    )

    cv2.putText(
        annotated,
        "COUNTER AREA",
        (COUNTER_X1 + 10, COUNTER_Y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        3
    )

    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()

        for box, track_id in zip(boxes, ids):

            x1, y1, x2, y2 = box

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            person_id = int(track_id)

            inside_counter = (
                COUNTER_X1 <= center_x <= COUNTER_X2
                and
                COUNTER_Y1 <= center_y <= COUNTER_Y2
            )

            if inside_counter:

                if person_id not in entry_time:
                    entry_time[person_id] = time.time()

                stay_time = time.time() - entry_time[person_id]

                # Show timer
                cv2.putText(
                    annotated,
                    f"{stay_time:.1f}s",
                    (center_x, center_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

                # Alert after 10 sec
                if stay_time > 10 and person_id not in alerted:

                    print(
                        f"ALERT: PERSON {person_id} LOITERING FOR {stay_time:.1f} SECONDS"
                    )

                    report_data.append([
                        person_id,
                        round(stay_time, 2)
                    ])

                    alerted.add(person_id)

            else:

                if person_id in entry_time:
                    del entry_time[person_id]

    # Show active alert on screen
    if len(alerted) > 0:

        cv2.putText(
            annotated,
            "LOITERING ALERT!",
            (50, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0, 0, 255),
            4
        )

    cv2.imshow("Loitering Detection", annotated)

    key = cv2.waitKey(1)

    if key & 0xFF == ord("q"):
        print("Stopped By User")
        break

# ==========================
# SAVE CSV REPORT
# ==========================

with open("loitering_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Person ID",
        "Loitering Time (Seconds)"
    ])

    writer.writerows(report_data)

print("=================================")
print("Total Records:", len(report_data))
print("Report Saved: loitering_report.csv")
print("=================================")

cap.release()
cv2.destroyAllWindows()