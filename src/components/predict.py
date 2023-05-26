from ultralytics import YOLO
import glob
import os
import shutil
import subprocess


directory_path = "runs/detect/predict"
if os.path.exists(directory_path):
    shutil.rmtree(directory_path)


img_path = 'Bike-Helmet-Detection-2/test/images'
image_path='D:\Documents\Projects\AI-Camera-Implementation\Testdata\Helmet.jpg'
command='yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.5 source={}'.format(image_path)
output = subprocess.check_output(command.split())
print('Needed Result: ',output)
num_objects = output.decode('utf-8').count('Helmet')

print('Number of objects detected: {}'.format(num_objects))



