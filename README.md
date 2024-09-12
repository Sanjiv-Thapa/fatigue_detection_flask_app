# Fatigue Detection System

This project is a **Fatigue Detection System** that utilizes a convolutional neural network (CNN) model to analyze video inputs for signs of fatigue. The model processes video frames to detect whether a person's eyes are closed and their mouth is open, which are potential indicators of drowsiness. The detection logic is based on the PERCLOS (Percentage of Eye Closure) and POM (Percentage of Mouth Opening) metrics.

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

The system processes a video input to determine if the person in the video is showing signs of fatigue. It uses MTCNN (Multi-task Cascaded Convolutional Networks) for face detection and a pre-trained CNN model to predict whether the eyes are open or closed and whether the mouth is open or closed.

### Fatigue Detection Logic

The detection is based on two metrics:

1. **PERCLOS (Percentage of Eye Closure)**: Measures the proportion of time the eyes are closed.
2. **POM (Percentage of Mouth Opening)**: Measures the proportion of time the mouth is open.

If **PERCLOS** exceeds 50% or **POM** exceeds 50%, the system detects fatigue.

## Technologies Used

- Python
- TensorFlow/Keras (for the CNN model)
- Flask (for the web application)
- OpenCV (for video frame processing)
- MTCNN (for face, eye, and mouth detection)

## Usage

1. **Upload video**: From the home page, upload a video file. The video should clearly capture the person's face for accurate fatigue detection.

2. **Processing**: The system will extract frames from the video, detect faces, and use the CNN model to analyze whether the eyes and mouth are open or closed.

3. **Results**: After processing, the system will calculate PERCLOS and POM. If fatigue is detected (based on the metrics), a message will indicate the detection of fatigue; otherwise, it will show that the person is alert.



## Model Explanation
The CNN model used in this project is designed to classify facial features:

1. **Eyes (Open/Closed)**: The model identifies whether a person's eyes are open or closed in each frame of the video.
2. **Mouth (Open/Closed)**: The model detects whether the person's mouth is open, a common sign of yawning, which is associated with fatigue.

## Metrics
1. **PERCLOS (Percentage of Eye Closure)**: Measures the proportion of time the eyes are closed during the video.
2. **POM (Percentage of Mouth Opening)**: Measures the proportion of time the mouth is open during the video.
The system detects fatigue if PERCLOS > 50% or POM > 50%, indicating potential drowsiness.

## Preprocessing
The preprocessing steps include:

1. **Frame Extraction**: Extracts frames from the video at regular intervals.
2. **Face Detection**: Detects faces in each frame using MTCNN.
3. **Feature Extraction**: Identifies key points like eyes and mouth for further analysis.
4. **Resizing**: Resizes the detected eye and mouth regions to the appropriate size for input into the CNN model.
5. **Prediction**: The CNN model classifies each frame as eyes open/closed and mouth open/closed.

## Results
Once the system finishes analyzing the video, it displays one of the following results:

1. **Fatigue Detected**: If either PERCLOS > 50% or POM > 50%.
2. **No Fatigue Detected**: If the user is alert based on the analyzed metrics.


## Directory Structure

```plaintext
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

To run this project locally, follow these steps:

### Clone the Repository

```bash
git clone https://github.com/your-username/fatigue_detection_app.git
cd fatigue_detection_app
### Install Dependencies
pip install -r requirements.txt
Run the Application
python app.py
