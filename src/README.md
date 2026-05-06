# 🦾 Bionic Hand Firmware

This folder contains the core software architecture for a real-time bionic hand system using computer vision, gesture recognition, and servo control.

The system processes live camera input, recognizes hand gestures using MediaPipe, and maps them to predefined robotic hand movements.

---

## 🧠 System Overview

Camera Input → MediaPipe Recognition → Gesture Mapping → Servo Control → Hand Actuation

---

## 📁 Modules

### ⚙️ Control
Contains Python scripts responsible for servo control and gesture-to-motion mapping.

Includes predefined hand actions such as:
- open_hand
- close_hand
- peace_sign
- thumbs_up
- pointing
- rock_on

---

### 🧠 Models
Contains custom gesture recognition models built using MediaPipe landmark data.

These models are responsible for interpreting detected hand poses into usable gesture labels.

---

### 👁️ Vision
Handles camera input and real-time gesture detection using MediaPipe.

Responsibilities:
- Capturing video frames
- Extracting hand landmarks
- Passing data to recognition pipeline

---

### 🚀 Main.py
Entry point of the system.

Coordinates:
- Vision pipeline (camera + recognition)
- Gesture classification output
- Control layer (servo execution via gestures.py / control module)

---

### 📦 Requirements.txt
Lists all required Python dependencies for running the system, including:
- OpenCV
- MediaPipe
- NumPy
- other supporting libraries
