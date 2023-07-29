# Helmet Detection with YOLOv8 

This repository provides an implementation of an AI camera system that utilizes the YOLOv8 model for detecting whether a person in an uploaded image is wearing a helmet or not. This AI camera system is built using Python and several popular libraries for computer vision and deep learning.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [License](#license)

## Introduction

The AI camera implementation in this repository aims to automate the process of detecting whether a person in an image is wearing a helmet or not. It utilizes the YOLOv8 model, a state-of-the-art object detection algorithm, which is known for its accuracy and efficiency.

The YOLOv8 model is trained on a custom dataset that consists of images with annotated bounding boxes around the helmets. During inference, the model analyzes the uploaded image and predicts the presence of helmets by drawing bounding boxes around the detected regions.

## Installation

To set up the AI camera implementation locally, follow these steps:

1. Clone this repository to your local machine.
2. Ensure that you have Python 3.6 or higher installed.
3. Install the required dependencies by running the following command in the repository's root directory:

````shell
pip install -r requirements.txt
````

4. Download the pre-trained weights for the YOLOv8 model by visiting the official YOLO website or a compatible repository. Place the weights file in the `model_weights` directory.

## Usage

To use the AI camera system, follow these steps:

1. Start the web application by running the following command:
````shell
python app.py
````

2. Open a web browser and visit `http://localhost:5000`.
3. Upload an image using the provided interface.
4. Click the "Detect" button to process the image and display the detected bounding boxes around any detected helmets.
5. The result will be displayed on the web page, showing whether the person in the image is wearing a helmet or not.

## Model Training

If you wish to train the YOLOv8 model on a custom dataset or fine-tune the existing weights, follow these steps:

1. Prepare a dataset of images containing annotations for helmet bounding boxes.
2. Split the dataset into training and validation sets.
3. Modify the configuration file (`yolov8.cfg`) to suit your dataset and training preferences.
4. Run the training script:

````shell
python main.py
````

5. Monitor the training progress and adjust hyperparameters as needed.
6. Once the training is complete, the final weights will be saved in the `runs/detect/results/weights/best.pt` directory.

## License

The AI camera implementation is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to your requirements.

Please note that while the AI camera system aims to detect whether a person is wearing a helmet or not, it may not provide perfect accuracy in all scenarios. It is important to exercise caution and rely on multiple safety measures when assessing helmet usage.

For more information, refer to the documentation and comments within the codebase. If you encounter any issues or have suggestions for improvements, please open an issue in the repository.





Website UI
<img width="960" alt="image" src="https://github.com/shrutimary15/Safe-skull/assets/90182268/8bbc43be-0ef3-44ae-bbb4-4af6c6d4ba5b">
<img width="960" alt="image" src="https://github.com/shrutimary15/Safe-skull/assets/90182268/40f11d01-2982-4b14-92d9-d5766088deaa">
<img width="960" alt="image" src="https://github.com/shrutimary15/Safe-skull/assets/90182268/b9ec6016-a17b-43ea-89b5-672862d6f223">



