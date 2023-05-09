from ultralytics import YOLO
model = YOLO("C:/Users/Lenovo/Documents/AI-Camera-Implementation/yolov8s.pt")
results = model.predict("C:/Users/Lenovo/Documents/AI-Camera-Implementation/Bike-Helmet-Detection-2/test/images/BikesHelmets18_png_jpg.rf.84a3bd2569cd63e920de9c89d731bd7c.jpg")

print(model.classes)
result = results[0]
output = []
for box in result.boxes:
        x1, y1, x2, y2 = [
          round(x) for x in box.xyxy[0].tolist()
        ]
        class_id = box.cls[0].item()
        prob = round(box.conf[0].item(), 2)
        output.append([
          x1, y1, x2, y2, result.names[class_id], prob
        ])
print(output)
