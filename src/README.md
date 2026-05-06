# Bionic Hand Firmware

This README contains the firmware for MK0 of my Bionic Hand Project. Below are brief descriptions of each file:

## Roadmap

### Step 1 - Gestures
Create `gestures.py` containing these hand gestures:
- close_hand
- open_hand
- peace_sign
- thumbs_up
- pointing
- rock_on

Create a `main.py` alongside it to bind keyboard keys to each gesture.

### Step 2 - Computer Vision
Implement OpenCV to capture my hand gestures from a camera feed called 'camera.py'.

### Step 3 - Gesture Recognition
Implement MediaPipe to identify captured gestures and run the gestures automatically on the hand without keyboard input called 'recognition.py'.
