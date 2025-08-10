#Intelligent Real-Time Surveillance System using YOLOv8

Intelligent Real-Time Surveillance System using YOLOv8

This project implements **Intelligent Real-Time Surveillance System** using the YOLOv8 model (Ultralytics) and OpenCV, with the ability to **record detections as a video file**.

---

## 🚀 Features
- Detects **80 common objects** from the COCO dataset  
- Runs in **real-time** from your webcam  
- Saves detections to an `.mp4` video file  
- Easy to run and customize for other datasets  

---

## 🛠 Installation
1. **Clone the repository**  
```bash
git clone https://github.com/Faizanahmed246/IIIT-H-Internship
cd yolov8-realtime-detection
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

---

## ▶ Usage
Run the script:
```bash
python yolov8_webcamwithrecord.py
```

- Press **`q`** to stop recording and exit.
- Video will be saved in the current folder as:
```
yolov8_detections_YYYYMMDD_HHMMSS.mp4
```

---

## 📂 Project Structure
```
.
├── README.md
├── requirements.txt
├── yolov8_webcam_record.py and yolov8_webcamwithrecord.py
```

---

---

## 📚 How It Works
1. Loads YOLOv8 **nano model** (`yolov8n.pt`) pre-trained on COCO dataset  
2. Captures live video feed from webcam  
3. Runs object detection on each frame  
4. Draws bounding boxes & labels  
5. Saves annotated video to disk  

---

## 💡 Customization
- To detect **custom objects**, train YOLOv8 on your own dataset and replace `yolov8n.pt` with your trained weights.
- Change webcam source:
```python
cap = cv2.VideoCapture(0)  # Change 0 to video path or different camera index
This project is open-source and free to use for educational purposes.

