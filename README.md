# ✋ Neon Gesture Controller

A futuristic **hand gesture controller for Windows** built with Python, OpenCV, CVZone, and MediaPipe.

Control your PC and launch applications or websites using simple hand gestures — without using your mouse.

The project also includes a standalone **neon-style HUD dashboard** designed for a secondary monitor.

## ✨ Features

* ✋ Real-time hand tracking
* 🧠 Gesture recognition
* 🚀 Gesture-based application launching
* 🌐 Website launching
* 🖥️ Windows application control
* 🎨 Futuristic neon HUD
* 💎 Glassmorphism dashboard
* ⏱️ Gesture cooldown system
* 🖱️ No cursor movement
* 📷 Webcam-based tracking
* ⚡ Lightweight local processing

## 🎮 Gesture Controls

| Gesture           | Action               |
| ----------------- | -------------------- |
| ✌️ Peace          | YouTube              |
| ☝️ Pointer        | ChatGPT              |
| 🤘 Rock           | Instagram            |
| 🖐️ Three Fingers | WhatsApp Web         |
| 🤙 Pinky          | Windows Task Manager |

## 🛠️ Built With

* Python
* OpenCV
* CVZone
* MediaPipe
* HTML
* CSS
* JavaScript

## 🧩 How It Works

```text
             📷 WEBCAM
                 │
                 ▼
        ┌─────────────────┐
        │   OpenCV        │
        │   Camera Feed   │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   CVZone /      │
        │   Hand Tracking │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Gesture         │
        │ Classifier      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Action Launcher │
        └────────┬────────┘
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    YouTube   ChatGPT   WhatsApp
```

## 📁 Project Structure

```text
NeonGestureController/
│
├── main.py
├── dashboard.html
├── requirements.txt
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/NeonGestureController.git
```

Enter the project directory:

```bash
cd NeonGestureController
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the controller:

```bash
python main.py
```

The dashboard will open automatically and the webcam-based gesture controller will start.

## ⚙️ Requirements

* Windows
* Python 3.10+
* Webcam
* Internet connection for web-based actions
* Google Chrome recommended

## 🔧 Customization

Gesture mappings can be modified inside:

```python
classify_hand_gesture()
```

Actions can be changed inside the gesture action section of `main.py`.

You can also completely redesign `dashboard.html` without changing the gesture-recognition engine.

## 🔒 Privacy

The gesture recognition runs locally on your computer.

The project does not upload webcam footage to a remote server.

## 🚧 Future Ideas

* 📱 Android companion application
* 📊 Live CPU/RAM/GPU monitoring
* 🖥️ Multi-monitor integration
* ✋ Custom gesture profiles
* ⚡ Advanced Windows automation
* 🎮 Game controls
* 🧠 Local AI integration
* 🔄 Real-time PC ↔ Android communication

## ⭐ Support

If you find this project interesting, consider giving it a ⭐ on GitHub.

Fork it, customize the gestures, and build your own futuristic PC controller.

---

**Built with Python + Computer Vision + a little futuristic madness. ⚡**

## Project Notes

Gesture recognition is processed locally through the webcam pipeline. The dashboard is separated from the recognition workflow so the interface can be refined independently.
