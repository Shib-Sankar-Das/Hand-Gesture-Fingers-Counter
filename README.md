# Hand Gesture Fingers Counter 

HandGestureFingersCounter is a Python-based project using OpenCV and MediaPipe to recognize hand gestures and display the corresponding count of fingers raised. The application utilizes real-time hand tracking and finger detection to interpret hand signs and overlays images onto a live webcam feed, displaying the finger count visually.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Project Approach](#project-approach)
3. [Features](#features)
4. [Dependencies](#dependencies)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Screenshots](#screenshots)
8. [Future Improvements](#future-improvements)

---

## Introduction
Hand gesture recognition is a powerful tool in various fields, including sign language interpretation, human-computer interaction, and interactive gaming. This project aims to create a hand gesture-based counter that detects the number of fingers held up and displays the count in real-time. The project uses MediaPipe's hand tracking module to detect and track hand landmarks and OpenCV for computer vision processing.

## Project Approach
1. **Hand Detection and Tracking**: Using MediaPipe's `Hands` module, the program detects hands in the webcam feed. The hand detector is initialized with parameters for detection confidence and tracking confidence to ensure robust real-time detection.
2. **Finger Counting**: Based on the hand landmarks, the program identifies which fingers are raised. Using specific landmark positions, it determines the number of raised fingers.
3. **Overlaying Images**: Based on the detected finger count, a corresponding image is displayed on the screen.
4. **Performance Tracking**: The program calculates and displays the FPS (Frames per Second) to monitor performance.

## Features
- Real-time hand detection and tracking
- Accurate finger counting based on hand landmarks
- Dynamic overlay of images on webcam feed based on finger count
- FPS calculation to monitor performance

## Dependencies
- Python 3.7 or higher
- OpenCV
- MediaPipe

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/HandGestureFingersCounter.git
    ```

2. **Install Required Packages**:
    Install the required dependencies using pip:
    ```bash
    pip install opencv-python mediapipe
    ```

3. **Prepare Overlay Images**:
    - Place images in the `count` folder.
    - Ensure images have a transparent background and are resized to fit the screen.

## Usage
1. Run the program:
    ```bash
    python FingureCounter.py
    ```

2. **Real-Time Gesture Recognition**:
    - Open the webcam feed and show the number of fingers raised based on hand landmarks.
    - The image overlay and FPS counter will be displayed in the live feed.

## Screenshots
![Screenshot 2024-11-08 155759](https://github.com/user-attachments/assets/7ea2e274-589e-4785-a492-618429c90c91)


## Future Improvements
- Adding support for multiple gestures
- Creating a GUI for more user-friendly control
- Integrating with other applications for enhanced interactivity
- Adding gesture-based control for other devices or systems

