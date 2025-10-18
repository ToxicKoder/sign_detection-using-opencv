✋ Hand Gesture Recognition using MediaPipe and OpenCV

This project demonstrates real-time hand gesture recognition using MediaPipe and OpenCV.
It detects and tracks hand landmarks through a webcam feed, processes them into feature points, and predicts gestures using a trained Random Forest Machine Learning model.

🧩 Overview

The system captures hand movements via webcam, identifies 21 hand landmarks using MediaPipe, and classifies the gestures into predefined categories.
It provides an efficient, accurate, and real-time gesture recognition experience.

⚙️ Features

✅ Real-time hand detection and tracking
✅ Live gesture prediction using a trained model
✅ Bounding box and gesture labels displayed on screen
✅ Smooth performance and minimal latency

🧠 Technologies Used

🟦 Python 3
📸 OpenCV – Video capture and visualization
✋ MediaPipe – Hand landmark detection
🔢 NumPy – Numerical feature processing
📦 Pickle – Model storage and loading
🌲 Scikit-learn – Random Forest classification

🚀 How to Run

🔴IMPORTANT : FOR THE DATSET USE THE FILE "collect_images.py" TO CREATE THE DATASET ( THE FILE WILL RUN AND CREATE A 100 SAMPLES FOR THE 3 CASES AS IT IS TRAINED LIKE THAT)

Clone this repository and open the project folder.

Install the required libraries using
pip install opencv-python mediapipe numpy scikit-learn

Run the script with all the files included as given
test_classifier.py

The webcam will open and start detecting gestures in real time.

Press SPACEBAR to exit the program.

📊 Model Details

Algorithm: Random Forest Classifier

Input Features: 42 (21 landmarks × 2 coordinates)

Recognized Gestures: A, B, L
