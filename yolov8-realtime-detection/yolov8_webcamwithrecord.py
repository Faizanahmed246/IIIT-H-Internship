
# Real-Time Object Detection using YOLOv8 with Video Recording


from ultralytics import YOLO
import cv2
import datetime


model = YOLO("yolov8n.pt")  # Pre-trained on COCO dataset

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30  # fallback to 30 if not detected


timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
out = cv2.VideoWriter(
    f"yolov8_detections_{timestamp}.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height)
)

print("Press 'q' to stop recording and exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break


    results = model(frame)

   
    annotated_frame = results[0].plot()

    
    out.write(annotated_frame)

    
    cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved successfully!")
