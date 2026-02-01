# 🖐️ Hand Gesture Hill Climb Game 🚗⛰️

Control **Hill Climb Lite / Hill Climb Racing (PC)** using **hand gestures** via webcam.

This project allows playing an existing hill climbing game **without keyboard**, using real-time hand gesture recognition.

---

## 🚀 Features
- Real-time hand tracking using webcam
- Simple open-hand and closed-fist gestures
- Works with Hill Climb Lite (PC / Emulator)
- Smooth accelerate and brake control
- Beginner-friendly implementation

---

## 🧰 Tech Stack
- Python 3.10
- OpenCV
- MediaPipe
- PyAutoGUI

---

## ✋ Gesture Controls

| Hand Gesture | Action | Key |
|-------------|--------|-----|
| ✋ Open Hand (Palm Open) | Accelerate | Right Arrow (→) |
| ✊ Closed Fist | Brake | Left Arrow (←) |
| ❌ No Hand | Idle | None |

---

## 🧠 Working Principle

1. Webcam captures live video input.
2. MediaPipe detects hand landmarks in real time.
3. Gesture (open hand / closed fist) is identified.
4. Gesture is mapped to keyboard key events.
5. Hill Climb game responds as if keys were pressed manually.

---

## ⚙️ Setup (Windows)

### 1️⃣ Python Installation
Download **Python 3.10.11**  
✔ Make sure **Add Python to PATH** is checked during installation.

Check installation:
```bash
python --version
2️⃣ Clone Repository
git clone https://github.com/USERNAME/hand-gesture-hill-climb.git
cd hand-gesture-hill-climb
3️⃣ (Optional) Virtual Environment
python -m venv hill_env
hill_env\Scripts\activate
4️⃣ Install Required Libraries
python -m pip install opencv-python mediapipe pyautogui
▶️ Run the Project
Open Hill Climb Lite in window mode

Keep the game window in focus

Run the program:

python gesture_control.py
Show hand gestures in front of webcam:

✋ Open hand → Accelerate

✊ Closed fist → Brake

Press Q to exit.

📁 Project Structure
hand-gesture-hill-climb/
│
├── gesture_control.py   # Main gesture control script
└── README.md            # Project documentation
📝 Notes
Use only one hand

Ensure good lighting

Game must support Left / Right arrow keys

Keep webcam stable for best detection

🎓 Academic Use
Suitable for:

Mini Project

Computer Vision Project

Human Computer Interaction (HCI)

AI-based Game Control Demonstration

👤 Author
sanya-1612

📜 License
This project is created for educational purposes only.

