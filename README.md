# Neon Gesture Controller

A Windows hand-gesture controller that uses a webcam, computer vision, and gesture mappings to trigger selected PC actions and web shortcuts.

## Overview

GUESTURE-ASSISTANT combines real-time hand tracking with a separate neon-style HUD. The webcam provides the input, OpenCV and the CVZone/MediaPipe stack process the hand data, and the recognized gesture is translated into a configured action.

The project is designed as a local computer-vision experiment with a visual interface that can evolve independently from the recognition pipeline.

## Features

- Real-time hand tracking
- Gesture recognition
- Gesture-based action launching
- Website shortcuts
- Windows application actions
- Neon HUD dashboard
- Glassmorphism-inspired interface
- Gesture cooldown handling
- Webcam input
- Local computer-vision processing

## Current Gesture Map

| Gesture | Action |
| --- | --- |
| Peace | YouTube |
| Pointer | ChatGPT |
| Rock | Instagram |
| Three Fingers | WhatsApp Web |
| Pinky | Windows Task Manager |

The gesture-to-action mappings can be changed in the controller implementation.

## Architecture

```text
Webcam
  |
  v
OpenCV
  |
  v
CVZone / MediaPipe
  |
  v
Hand and Gesture Recognition
  |
  v
Action Mapping
  |
  v
Windows / Web Action
```

The recognition pipeline runs locally. The dashboard is kept separate from the core recognition flow so the visual layer can be refined without replacing the computer-vision logic.

## Technology Stack

- Python 3.10+
- OpenCV
- CVZone
- MediaPipe
- HTML
- CSS
- JavaScript

## Getting Started

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Start the controller:

```bash
python main.py
```

A working webcam is required for gesture recognition.

## Privacy

Gesture recognition is processed locally on the computer. The project does not intentionally upload webcam footage to a remote server.

Websites or online services launched by gestures may communicate with their own services as normal.

## Customization

The controller can be extended by changing:

- Gesture-to-action mappings
- Cooldown timing
- Dashboard visuals
- Supported Windows actions
- Additional gesture profiles

## Future Ideas

- Custom gesture profiles
- Multi-monitor support
- System resource HUD
- Game controls
- Android companion
- Local AI integration
- PC to Android communication

## Creator

Made by **JebinTech**.

---
Built with computer vision and a focused futuristic interface by **JebinTech**.
