from ultralytics import YOLO
import glob
import os



dir_path = 'runs/detect/predict/*'
if os.path.exists('runs/detect/predict'):
    for img in glob.glob(dir_path):
      os.remove(img)
    os.rmdir('runs/detect/predict')
img_path = 'Bike-Helmet-Detection-2/test/images'
os.system('yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.5 source={}'.format(img_path))
