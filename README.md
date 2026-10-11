# GUESTURE-ASSISTANT

A Windows desktop utility that uses webcam-based hand tracking to launch configured websites and desktop tools through predefined gestures.

## Overview

GUESTURE-ASSISTANT uses OpenCV and CVZone/MediaPipe to detect a hand, classify a small set of gestures, and trigger the matching action. A camera preview displays the detected gesture and action status.

## Features

- Live webcam hand tracking
- Gesture smoothing to reduce accidental triggers
- Per-gesture cooldowns to prevent repeated launches
- Configurable website and desktop-action mappings in `main.py`
- Optional audio prompts from the local `sounds/` directory
- Optional local dashboard in `dashboard.html`
- Keyboard exit with `Q` or `Esc`

## Gesture Mapping

| Gesture | Default action |
| --- | --- |
| Peace | Open YouTube |
| Index finger | Open ChatGPT |
| Index and pinky | Open Instagram |
| Three fingers | Open WhatsApp Web |
| Pinky only | Open Windows Task Manager |

Review the action mapping in the source before running the controller. Website shortcuts open external services in your browser.

## Requirements

- Windows
- Python compatible with the installed MediaPipe and OpenCV versions
- A working webcam
- Optional: Google Chrome, local sound files, and `dashboard.html`

## Installation

Open PowerShell in the repository directory and create a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the controller:

```powershell
python main.py
```

The webcam window displays the detected gesture and current action. Press `Q` or `Esc` to stop the application.

## Project Files

- `main.py` — webcam loop, gesture classification, and action handlers
- `dashboard.html` — optional local dashboard
- `sounds/` — optional WAV prompts

The application resolves dashboard and sound paths relative to the script location, so it does not depend on the terminal's current working directory.

## Troubleshooting

- **Camera does not open:** close other applications using the webcam and check Windows camera permissions.
- **A sound is missing:** verify that the expected WAV file exists in `sounds/`; missing sounds are reported as warnings.
- **Chrome is not installed:** website shortcuts use the system's default browser.
- **Gesture triggers repeatedly:** adjust the cooldown and smoothing settings in `main.py`.

## Privacy and Safety

Camera frames are processed locally by the application. Recognized gestures can launch websites or Windows tools; review these mappings before use and close the application when webcam tracking is no longer needed.

## Maintainer

**JebinTech**
