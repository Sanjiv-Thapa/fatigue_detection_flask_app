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
