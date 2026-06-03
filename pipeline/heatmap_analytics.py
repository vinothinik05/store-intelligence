from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("dataset/CAM 2.mp4")

heatmap = None

while True:

    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    if heatmap is None:
        heatmap = np.zeros((h, w), dtype=np.float32)

    results = model.track(
        frame,
        persist=True,
        classes=[0]
    )

    annotated = results[0].plot()

    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu().numpy()

        for box in boxes:

            x1, y1, x2, y2 = box

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            cv2.circle(
                heatmap,
                (center_x, center_y),
                25,
                1,
                -1
            )

    heatmap_blur = cv2.GaussianBlur(
        heatmap,
        (51, 51),
        0
    )

    heatmap_norm = cv2.normalize(
        heatmap_blur,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    heatmap_color = cv2.applyColorMap(
        heatmap_norm.astype(np.uint8),
        cv2.COLORMAP_JET
    )

    overlay = cv2.addWeighted(
        frame,
        0.6,
        heatmap_color,
        0.4,
        0
    )

    cv2.imshow(
        "Store Heatmap Analytics",
        overlay
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()