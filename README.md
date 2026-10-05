# ✋ Neon Gesture Controller

A futuristic Windows hand-gesture controller built with Python, OpenCV, CVZone, and MediaPipe.

Use webcam-based hand gestures to trigger PC actions and launch selected applications or websites, with a separate neon HUD for visual feedback.

## ✨ Features

- ✋ Real-time hand tracking
- 🧠 Gesture recognition
- 🚀 Gesture-based action launching
- 🌐 Website shortcuts
- 🖥️ Windows application actions
- 🎨 Neon HUD dashboard
- 💎 Glassmorphism-inspired interface
- ⏱️ Gesture cooldown handling
- 📷 Webcam input
- ⚡ Local computer-vision processing

## 🎮 Current Gesture Map

| Gesture | Action |
| --- | --- |
| ✌️ Peace | YouTube |
| ☝️ Pointer | ChatGPT |
| 🤘 Rock | Instagram |
| 🖐️ Three Fingers | WhatsApp Web |
| 🤙 Pinky | Windows Task Manager |

Gesture mappings can be changed in the controller implementation.

## 🧠 Architecture

```text
Webcam
  ↓
OpenCV
  ↓
CVZone / MediaPipe
  ↓
Hand & Gesture Recognition
  ↓
Action Mapping
  ↓
Windows / Web Action
```

The recognition pipeline runs locally. The dashboard is kept separate so the visual interface can evolve without replacing the core recognition workflow.

## 🛠️ Stack

- Python 3.10+
- OpenCV
- CVZone
- MediaPipe
- HTML
- CSS
- JavaScript

## 🚀 Getting Started

Install the Python dependencies listed by the project:

```bash
pip install -r requirements.txt
```

Then start the controller:

```bash
python main.py
```

A working webcam is required for gesture recognition.

## 🔒 Privacy

Gesture recognition is processed locally on the computer. The project does not intentionally upload webcam footage to a remote server.

Websites launched by gestures may of course communicate with their own services.

## 🔧 Customization

You can extend the project by changing:

- Gesture-to-action mappings
- Cooldown timing
- Dashboard visuals
- Supported Windows actions
- Additional gesture profiles

## 🚧 Future Ideas

- Custom gesture profiles
- Multi-monitor support
- System resource HUD
- Game controls
- Android companion
- Local AI integration
- PC ↔ Android communication

## Creator

Made by **JebinTech**.

---
Built with computer vision and a futuristic interface by **JebinTech**.
