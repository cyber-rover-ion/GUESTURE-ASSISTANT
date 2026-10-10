# GUESTURE-ASSISTANT

A webcam-based hand-gesture controller for triggering configured desktop actions and website shortcuts on Windows.

## Overview

GUESTURE-ASSISTANT uses Python and computer-vision libraries to detect hand landmarks and map recognized gestures to predefined actions. A separate browser-based dashboard provides a visual interface for the project.

## Features

- Live webcam input
- Hand landmark tracking and gesture recognition
- Gesture-to-action mappings
- Windows application actions and website shortcuts
- Local computer-vision processing
- Browser-based dashboard
- Gesture cooldown handling

## Default Gesture Mapping

| Gesture | Action |
| --- | --- |
| Peace | YouTube |
| Pointer | ChatGPT |
| Rock | Instagram |
| Three fingers | WhatsApp Web |
| Pinky | Windows Task Manager |

Mappings depend on the current controller implementation and can be adjusted in the source code.

## Architecture

```text
Webcam
  |
  v
OpenCV / MediaPipe
  |
  v
Hand Landmark and Gesture Recognition
  |
  v
Configured Action Mapping
  +--> Desktop Actions
  +--> Website Shortcuts
```

## Technology

- Python
- OpenCV
- MediaPipe
- CVZone
- HTML, CSS, and JavaScript

## Installation

Install the dependencies listed in the repository:

```bash
pip install -r requirements.txt
```

Start the controller:

```bash
python main.py
```

A working webcam is required. Review the configured actions before running the controller.

## Privacy

Gesture recognition is designed to process webcam input locally. Websites opened by shortcuts operate under their own privacy policies and terms.

## Maintainer

**JebinTech**
