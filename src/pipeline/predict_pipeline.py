import os



class PredictPipelineConfig:
    model_path=os.path.join('runs/detect/train/weights','best.pt')

class PredictPipeline:
    def __init__(self):
        self.model_path_config=PredictPipelineConfig()
    def predict_pipeline(self,image_path):
        os.system('yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.5 source={}'.format(image_path))
