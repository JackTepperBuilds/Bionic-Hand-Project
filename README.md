## MK0 GIF

### Gesture Recognition
<img width="640" height="396" alt="20260504_141202(1)" src="https://github.com/user-attachments/assets/2e550a3d-35d1-4758-a8a7-08d186947fc2" />

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

---

## 📁 Project Structure

- `src/` → Core system code (vision, control, models)
- `docs/` → Technical documentation (BOM, MK reports, lessons learned)
- `assets/` → Images and videos of system demos and assembly

---

## 🚀 System Evolution

The project is developed in iterative versions:

- **MK0** → Initial prototype with basic MediaPipe gesture-to-servo mapping
- **MK1** → Refactored MK0 code in C++, improved control, 17 degrees of freedom, and redesigned mechanical build

Each version is tracked using Git tags and documented in the `docs/` folder.

---

