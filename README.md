# GUESTURE-ASSISTANT

A Windows hand-gesture controller that uses a webcam and computer vision to trigger configured desktop and web actions.

## Overview

GUESTURE-ASSISTANT uses Python, OpenCV, and MediaPipe-based hand tracking to recognize gestures from a webcam feed. Recognized gestures are mapped to predefined actions, while a separate browser-based dashboard provides the visual interface.

## Features

- Real-time webcam input
- Hand landmark tracking
- Gesture recognition
- Configurable gesture-to-action mappings
- Windows application actions
- Website shortcuts
- Local computer-vision processing
- Neon-style dashboard
- Gesture cooldown handling

## Current Gesture Mapping

| Gesture | Action |
| --- | --- |
| Peace | YouTube |
| Pointer | ChatGPT |
| Rock | Instagram |
| Three Fingers | WhatsApp Web |
| Pinky | Windows Task Manager |

The mappings can be changed in the controller implementation.

## Architecture

```text
Webcam
  |
  v
OpenCV / MediaPipe
  |
  v
Hand and Gesture Recognition
  |
  v
Action Mapping
  |
  +--> Windows Actions
  +--> Web Shortcuts
```

The recognition process runs locally. The dashboard is kept separate from the core controller so the interface can be changed independently.

## Technology

- Python 3.10+
- OpenCV
- CVZone
- MediaPipe
- HTML
- CSS
- JavaScript

## Setup

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Then start the controller:

```bash
python main.py
```

A working webcam is required.

## Privacy

The project processes gesture input locally and does not intentionally upload webcam footage to a remote server. Any website opened through a gesture communicates with that website according to its own service.

## Creator

Made by **JebinTech**.
