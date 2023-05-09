# Bike Helmet Detection > more-preprocessing-augmentation
https://universe.roboflow.com/bike-helmets/bike-helmet-detection-2vdjo

Provided by a Roboflow user
License: Public Domain

## Background Information
This dataset was curated and annotated by [Syed Salman Reza](https://github.com/syed-reza98). A custom dataset composed of two classes (With Helmet, Without Helmet). Main objetive is to identify if a Biker wearing Helmet or not.

The original custom dataset *(v1)* is composed of 1,371 images of people with and without bike helmets.

The dataset is available under the Public License.

![Example of an Annotated Image from the Dataset](https://i.imgur.com/XWrAEnS.jpeg)

## Getting Started
You can download this dataset for use within your own projects, or fork it into a workspace on Roboflow to create your own model.

## Dataset Versions
### Version 1 (v1) - 1,371 images
* Preprocessing: Auto-Orient and Resize (Stretch to 416x416)
* Augmentations: *Augmentations applied prior to import* - Bounding Box Blur (up to 10px)
* Training Metrics: Trained from the COCO Checkpoint in Public Models ("[transfer learning](https://blog.roboflow.com/a-primer-on-transfer-learning/)") on Roboflow
	* mAP = 74.4%, precision = 54.0%, recall = 77.0%

### Version 2 (v2) - 3,735 images
* Preprocessing: Auto-Orient and Resize (Stretch to 416x416)
* Augmentations: *Augmentations applied prior to import* - Bounding Box Blur.
	* *New augmentations*:
Outputs per training example: 3
Rotation: Between -30° and +30°
Shear: ±15° Horizontal, ±15° Vertical
Blur: Up to 1.5px
Mosaic: Applied
* Training Metrics: Trained from the COCO Checkpoint in Public Models ("[transfer learning](https://blog.roboflow.com/a-primer-on-transfer-learning/)") on Roboflow
	* mAP = 91.5%, precision = 65.1%, recall = 92.8%

Syed Salman Reza - [Github](https://github.com/syed-reza98)