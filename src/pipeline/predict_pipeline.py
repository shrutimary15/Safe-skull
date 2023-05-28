import os
from ultralytics import YOLO
import shutil
import cv2

class PredictPipelineConfig:
    model_path=os.path.join('runs/detect/train/weights','best.pt')

class PredictPipeline:
    def __init__(self):
        self.model_path_config=PredictPipelineConfig()

    def normalize_image(v_x,v_y,width,height):
        normalized_x=float(v_x)
        normalized_y=float(v_y)
        normalized_width=float(width)
        normalized_height=float(height)
        image_width,image_height=416,416
        # Calculate the coordinates of the bounding box in pixels
        x = int(normalized_x * image_width)
        y = int(normalized_y * image_height)
        w = int(normalized_width * image_width)
        h = int(normalized_height * image_height)

        # Calculate the coordinates of the rectangle's corners
        x1 = int(x - w/2)
        y1 = int(y - h/2)
        x2 = int(x + w/2)
        y2 = int(y + h/2)
        return x1,y1,x2,y2
    def predict_pipeline(image_path):
        directory_path = "runs/detect/predict"
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)

        os.system('yolo task=detect mode=predict model=runs/detect/train/weights/best.pt conf=0.5 source={}'.format(image_path))

        #Resizing Image
        image=cv2.imread(image_path)
        resized_image=cv2.resize(image,(416,416))

        model = YOLO('runs/detect/train/weights/best.pt')
        predictions = model(resized_image, save_txt=None)
        #{1 : without helmet, 0: with helmet}
        with open("runs/detect/predict/predicted_labels.txt", '+w') as file:
            for idx, prediction in enumerate(predictions[0].boxes.xywhn): # change final attribute to desired box format
                cls = int(predictions[0].boxes.cls[idx].item())
                # Write line to file in YOLO label format : cls x y w h
                file.write(f"{cls}, {prediction[0].item()}, {prediction[1].item()}, {prediction[2].item()}, {prediction[3].item()}\n")
                
                #Normalizing image
                x1,y1,x2,y2=PredictPipeline.normalize_image(prediction[0].item(),prediction[1].item(),prediction[2].item(),prediction[3].item())

                # Draw the rectangle on the image
                cv2.rectangle(resized_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Display the image with the rectangle
                
            cv2.imwrite(os.path.join(directory_path,'predicted.png'),resized_image)
        return os.path.join(directory_path,'predicted.png')

                
            