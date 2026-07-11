## MK0 GIF

### Gesture Recognition
<img width="654" height="368" alt="20260711_024246(1)" src="https://github.com/user-attachments/assets/af7bc7ac-7d19-4efc-9984-4e2d66e1bddb" />

---

# 🦾 Bionic Hand Project

A real-time bionic hand system controlled using computer vision, OpenCV, and MediaPipe running on a Raspberry Pi 5.

The system translates live hand gestures into robotic finger movements using a vision → recognition → control pipeline.

---

## 🔥 Demos

- 🎥 [Gesture Recognition Demo](https://www.youtube.com/shorts/l--I8Azhv_0)


## 🧠 System Overview

Camera Input → MediaPipe Hand Tracking → Gesture Recognition → Servo Control → Bionic Hand Actuation

---

## ⚙️ Tech Stack

- Python
- OpenCV
- MediaPipe
- Raspberry Pi 5
- PCA9685 Servo Driver
- MG995 Servos
- Raspberry Pi Camera Module 2

---

## 📁 Project Structure

- `src/` → Core system code (vision, control, models)
- `docs/` → Technical documentation (BOM, MK reports, lessons learned)
- `assets/` → Images and videos of system demos and assembly

---

## 🚀 System Evolution

The project is developed in iterative versions:

- **MK0** → Initial prototype with basic MediaPipe gesture-to-servo mapping
- **MK0.5** → OOP refactor of MK0 code featuring an error-based servo actuation algorithm to support future more complex gestures
- **MK0.6** → Multithreaded recognizer and hand controller with a safe exit using keyboard button 'd'
- **MK0.7** → Real-time MediaPipe landmark overlay to live feed
- **MK0.8** → Final MK0 iteration, implimenting gesture name and score onto real-time feed
- **MK1 (Planned)** → Refactored MK0 code in C++, improved control, 17 degrees of freedom, and redesigned mechanical build

Each version is tracked using Git tags and documented in the `docs/` folder.

---

