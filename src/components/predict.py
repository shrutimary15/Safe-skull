from ultralytics import YOLO
import os
import sys
import shutil
import cv2
from utils import normalize_image

directory_path = "runs/detect/predict"
if os.path.exists(directory_path):
    shutil.rmtree(directory_path)


img_path = "Testdata/download(1).jpeg"
os.system('yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.5 source={}'.format(img_path))
output_file = 'results.txt'

#Resizing Image
image=cv2.imread(img_path)
resized_image=cv2.resize(image,(416,416))

model = YOLO('runs/detect/train/weights/best.pt')
predictions = model(resized_image, save_txt=None)
#{1 : without helmet, 0: with helmet}
image_width,image_height,_=resized_image.shape
with open("runs/detect/predict/predicted_labels.txt", '+w') as file:
    for idx, prediction in enumerate(predictions[0].boxes.xywhn): # change final attribute to desired box format
        cls = int(predictions[0].boxes.cls[idx].item())
        # Write line to file in YOLO label format : cls x y w h
        file.write(f"{cls}, {prediction[0].item()}, {prediction[1].item()}, {prediction[2].item()}, {prediction[3].item()}\n")
        
        #Normalizing Image
        x1,y1,x2,y2=normalize_image(float(prediction[0].item()),float(prediction[1].item()),float(prediction[2].item()),float(prediction[3].item()))
        
        # Draw the rectangle on the image
        cv2.rectangle(resized_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display the image with the rectangle
        
    cv2.imwrite(os.path.join(directory_path,'predicted.png'),resized_image)

