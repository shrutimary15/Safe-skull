import os
from roboflow import Roboflow
rf = Roboflow(api_key="HJumpRJZ7Qwv1zCuFtXZ")
project = rf.workspace("bike-helmets").project("bike-helmet-detection-2vdjo")
dataset = project.version(2).download("yolov8")

os.system('wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt')



os.system('yolo task=detect mode=train model=yolov8s.pt imgsz=416 data=./Bike-Helmet-Detection-2/data.yaml epochs=300 batch=8 name=./results/')

