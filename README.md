# Fatigue Detection System

This project is a **Fatigue Detection System** that uses a convolutional neural network (CNN) model to analyze video input for signs of fatigue. The model processes video frames to detect whether a person's eyes are closed and their mouth is open, indicating potential drowsiness. The detection logic is based on the PERCLOS (Percentage of Eye Closure) and POM (Percentage of Mouth Opening) metrics.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Explanation](#model-explanation)
- [Preprocessing](#preprocessing)
- [Results](#results)
- [License](#license)

## Project Overview

The system takes a video as input and detects whether the person in the video is showing signs of fatigue. It uses the MTCNN (Multi-task Cascaded Convolutional Networks) for face detection and a pre-trained CNN model to predict whether the eyes are open or closed and the mouth is open or closed.

The fatigue detection is based on:
1. **PERCLOS (Percentage of Eye Closure)**: Measures the proportion of time the eyes are closed.
2. **POM (Percentage of Mouth Opening)**: Measures the proportion of time the mouth is open.

If either PERCLOS is higher than 50% or POM is higher than 50%, fatigue is detected.

## Technologies Used

- Python
- TensorFlow/Keras
- Flask (for web application)
- OpenCV (for video frame processing)
- MTCNN (for face, eye, and mouth detection)

## Directory Structure
fatigue_detection_app/
│
├── models/                    # Directory for the pre-trained model(s)
│   └── fatigue_model.h5        # Pre-trained fatigue detection model
│
├── static/                     # Static assets for the web app (CSS, JS, etc.)
│
├── templates/                  # HTML templates for Flask
│   ├── index.html              # Home page to upload video files
│   └── result.html             # Result page displaying fatigue detection result
│
├── uploads/                    # Directory for uploaded video files
│
├── utils/                      # Utility scripts for processing
│   ├── model_utils.py          # Helper functions for fatigue detection
│   └── dataset.py              # Dataset handling functions
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies for the project
├── README.md                   # Project description and instructions
└── .gitignore                  # Files to ignore in version control

## Installation

To run this project locally, follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/fatigue_detection_app.git
   cd fatigue_detection_app

## install dependencies
pip install -r requirements.txt

# download pretrained model
nsure the pre-trained model fatigue_model.h5 is located in the models/ directory. You can train your own model or use an existing model.
# run the application
python app.py
open in the browser :http://127.0.0.1:5000
## Usage
Upload Video: From the home page, upload a video file. The video should capture a person's face to detect fatigue accurately.
Processing: The system extracts frames from the video, detects faces, and then uses the CNN model to analyze whether the eyes and mouth are open or closed.
Results: After processing, the system calculates PERCLOS and POM. If fatigue is detected, it displays a message indicating the detection of fatigue. Otherwise, it shows that the person is alert.
## Model Explanation
The CNN model used in this project is designed to classify facial features:

Eyes (Open/Closed): The model identifies whether a person’s eyes are open or closed in each video frame.
Mouth (Open/Closed): The model also detects if the person’s mouth is open, which could indicate yawning, a common sign of fatigue.
## Metrics:
PERCLOS (Percentage of Eye Closure): This metric measures the proportion of time the eyes are closed during the video.
POM (Percentage of Mouth Opening): This metric measures the proportion of time the mouth is open during the video.
The system detects fatigue if PERCLOS > 50% or POM > 50%, indicating potential drowsiness.

## Preprocessing
The preprocessing steps include:

Frame Extraction: Extracts frames from the video at regular intervals.
Face Detection: Detects faces in each frame using MTCNN.
Feature Extraction: Identifies key points like eyes and mouth for further processing.
Resizing: Resizes the detected eye and mouth regions for input into the CNN model.
Prediction: The CNN model classifies each frame as eyes open/closed and mouth open/closed.
##  Results
Once the system finishes analyzing the video, it displays the following results:

Fatigue Detected: If either PERCLOS > 50% or POM > 50%.
No Fatigue Detected: If the user is alert based on the analyzed metrics.