import os
from ultralytics import YOLO
import shutil


class PredictPipelineConfig:
    model_path=os.path.join('runs/detect/train/weights','best.pt')

class PredictPipeline:
    def __init__(self):
        self.model_path_config=PredictPipelineConfig()
    def predict_pipeline(self,image_path):
        directory_path = "runs/detect/predict"
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)


        os.system('yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.5 source={}'.format(image_path))
        output_file = 'results.txt'
        model = YOLO('runs/detect/train/weights/best.pt')
        predictions = model(image_path, save_txt=None)
        #{1 : without helmet, 0: with helmet}
        with open("runs/detect/predict/predicted_labels.txt", '+w') as file:
            for idx, prediction in enumerate(predictions[0].boxes.xywhn): # change final attribute to desired box format
                cls = int(predictions[0].boxes.cls[idx].item())
                # Write line to file in YOLO label format : cls x y w h
                file.write(f"{cls}, {prediction[0].item()}, {prediction[1].item()}, {prediction[2].item()}, {prediction[3].item()}\n")