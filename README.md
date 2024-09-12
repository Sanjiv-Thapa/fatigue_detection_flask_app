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

## Installation

To run this project locally, follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/fatigue_detection_app.git
   cd fatigue_detection_app