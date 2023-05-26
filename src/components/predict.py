from ultralytics import YOLO
import glob
import os
import shutil

directory_path = "runs/detect/predict"
shutil.rmtree(directory_path)


img_path = 'Bike-Helmet-Detection-2/test/images'
image_path='D:\Documents\Projects\AI-Camera-Implementation\Testdata\download.jpeg'
command='yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.5 source={}'.format(image_path)
os.system(command)

print('Needed Result\n',output)


