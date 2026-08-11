import cv2
import time
import os
import sys
import subprocess
import webbrowser
import collections
import shutil
import winsound
from cvzone.HandTrackingModule import HandDetector

# ----------------------------------------------------
# Sound Helper
# ----------------------------------------------------
def play_sound(filename):
    """
    Plays a WAV file asynchronously from the 'sounds' folder.
    If the file does not exist or an error occurs, it prints
    a warning without crashing the application.
    """
    filepath = os.path.join("sounds", filename)
    if not os.path.exists(filepath):
        print(f"[Sound Error] File not found: {filepath}")
        return
    try:
        winsound.PlaySound(filepath, winsound.SND_ASYNC | winsound.SND_FILENAME)
    except Exception as e:
        print(f"[Sound Error] Could not play {filepath}: {e}")

# ----------------------------------------------------
# Application & URL Launcher Helpers
# ----------------------------------------------------
def open_dashboard():
    html_path = os.path.abspath("dashboard.html")
    webbrowser.open("file://" + html_path)

def get_chrome_path():
    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe")
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def open_url_in_chrome(url):
    chrome_path = get_chrome_path()
    if chrome_path:
        try:
            subprocess.Popen([chrome_path, url])
            return f"Opened {url} in Chrome"
        except Exception as e:
            webbrowser.open(url)
            return f"Opened default browser: {e}"
    else:
        try:
            os.system(f'start chrome "{url}"')
            return f"Launched Chrome via start command"
        except Exception:
            webbrowser.open(url)
            return "Opened default browser"

def open_antigravity():
    agy_path = shutil.which('agy')
    if agy_path:
        try:
            subprocess.Popen([agy_path])
            return "Launched Antigravity CLI/App"
        except Exception as e:
            pass
    try:
        os.system("start agy")
        return "Launched Antigravity via system start"
    except Exception as e:
        return f"Could not launch Antigravity: {e}"

def open_task_manager():
    try:
        subprocess.Popen(["taskmgr.exe"])
        return "Opened Windows Task Manager"
    except Exception as e:
        os.system("start taskmgr")
        return "Opened Task Manager via start command"

# ----------------------------------------------------
# Precise 5-Gesture Classifier
# ----------------------------------------------------
def classify_hand_gesture(fingers):
    """
    Classifies 5 distinct app launcher gestures:
    1. PEACE (✌️): Index & Middle extended -> Open YouTube
    2. POINTER (☝️): Index extended ONLY -> Open ChatGPT
    3. ROCK (🤘): Index & Pinky extended -> Open Instagram
    4. THREE_FINGERS (3️⃣): Index, Middle & Ring extended -> Open WHATSAPP
    5. PINKY_ONLY (🤙): Pinky extended ONLY -> Open Task Manager
    """
    if len(fingers) < 5:
        return "NONE"

    thumb, index, middle, ring, pinky = fingers

    # 1. Peace Sign (✌️): Index=1, Middle=1, Ring=0, Pinky=0
    if index == 1 and middle == 1 and ring == 0 and pinky == 0:
        return "PEACE"

    # 2. Pointer Finger Only (☝️): Index=1, Middle=0, Ring=0, Pinky=0
    if index == 1 and middle == 0 and ring == 0 and pinky == 0:
        return "POINTER"

    # 3. Pointer & Pinky / Rock Sign (🤘): Index=1, Pinky=1, Middle=0, Ring=0
    if index == 1 and pinky == 1 and middle == 0 and ring == 0:
        return "ROCK"

    # 4. Pointer, Middle & Ring (3️⃣): Index=1, Middle=1, Ring=1, Pinky=0
    if index == 1 and middle == 1 and ring == 1 and pinky == 0:
        return "THREE_FINGERS"

    # 5. Pinky Only (🤙): Pinky=1, Index=0, Middle=0, Ring=0
    if pinky == 1 and index == 0 and middle == 0 and ring == 0:
        return "PINKY_ONLY"

    return "NONE"

# ----------------------------------------------------
# Main Application
# ----------------------------------------------------
def main():
    print("=" * 65)
    print("      WEBCAM HAND TRACKING GESTURE APP LAUNCHER      ")
    print("=" * 65)
    print("Gestures:")
    print(" 1. Peace Sign (✌️)               -> Open YouTube")
    print(" 2. Pointer Finger Only (☝️)       -> Open ChatGPT")
    print(" 3. Pointer & Pinky (🤘)           -> Open Instagram")
    print(" 4. Pointer, Middle & Ring (3️⃣)    -> Open WHATSAPP")
    print(" 5. Pinky Only (🤙)               -> Open Windows Task Manager")
    print(" NOTE: Cursor does NOT move at all!")
    print("=" * 65)

    # Open dashboard and play startup sound
    open_dashboard()
    time.sleep(1.0)               # Short delay to allow dashboard to open
    play_sound("startup.wav")

    # Initialize OpenCV Webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[Error] Could not open webcam camera index 0.")
        return

    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

    # Initialize CVZone Hand Detector
    detector = HandDetector(detectionCon=0.85, maxHands=1)

    # Gesture history buffer for smoothing
    gesture_history = collections.deque(maxlen=4)

    # Cooldown timers (in seconds) to prevent multi-window spam
    last_action_times = {
        "PEACE": 0.0,
        "POINTER": 0.0,
        "ROCK": 0.0,
        "THREE_FINGERS": 0.0,
        "PINKY_ONLY": 0.0
    }
    cooldown_action = 3.0

    status_msg = "System Ready. Show hand gestures to launch applications."
    action_banner = ""
    action_banner_expire = 0.0
    action_banner_color = (0, 255, 255)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[Warning] Failed to grab frame from webcam.")
            break

        # Flip horizontally for natural selfie view
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # Detect Hand and Landmarks
        hands, frame = detector.findHands(frame, draw=True, flipType=False)

        current_gesture = "NONE"
        now = time.time()

        if hands:
            hand1 = hands[0]
            fingers = detector.fingersUp(hand1)

            raw_gesture = classify_hand_gesture(fingers)
            gesture_history.append(raw_gesture)

            # Smooth gesture classification
            most_common = collections.Counter(gesture_history).most_common(1)[0]
            if most_common[1] >= 2:
                current_gesture = most_common[0]

        else:
            gesture_history.clear()

        # ----------------------------------------------------
        # GESTURE ACTION LAUNCHERS (with audio before launch)
        # ----------------------------------------------------
        if current_gesture != "NONE":
            last_t = last_action_times.get(current_gesture, 0.0)

            if (now - last_t) > cooldown_action:
                # Play corresponding voice prompt BEFORE opening the app
                sound_map = {
                    "PEACE":        "youtube.wav",
                    "POINTER":      "chatgpt.wav",
                    "ROCK":         "instagram.wav",
                    "THREE_FINGERS":"whatsapp.wav",
                    "PINKY_ONLY":   "taskmanager.wav"
                }
                sound_file = sound_map.get(current_gesture)
                if sound_file:
                    play_sound(sound_file)

                res = ""
                if current_gesture == "PEACE":
                    res = open_url_in_chrome("https://www.youtube.com")
                    action_banner = "PEACE SIGN: OPENING YOUTUBE ✌️"
                    action_banner_color = (255, 215, 0)  # Gold

                elif current_gesture == "POINTER":
                    res = open_url_in_chrome("https://chatgpt.com")
                    action_banner = "POINTER FINGER: OPENING CHATGPT ☝️"
                    action_banner_color = (0, 255, 255)  # Cyan

                elif current_gesture == "ROCK":
                    res = open_url_in_chrome("https://www.instagram.com")
                    action_banner = "POINTER & PINKY: OPENING INSTAGRAM 🤘"
                    action_banner_color = (255, 20, 147)  # Deep Pink

                elif current_gesture == "THREE_FINGERS":
                    res = open_url_in_chrome("https://web.whatsapp.com")
                    action_banner = "3 FINGERS: OPENING WHATSAPPWEB 3️⃣"
                    action_banner_color = (138, 43, 226)  # Blue-Violet

                elif current_gesture == "PINKY_ONLY":
                    res = open_task_manager()
                    action_banner = "PINKY ONLY: OPENING TASK MANAGER 🤙"
                    action_banner_color = (0, 255, 127)  # Spring Green

                last_action_times[current_gesture] = now
                status_msg = f"[Action] {current_gesture} -> {res}"
                action_banner_expire = now + 2.5
            else:
                remaining = round(cooldown_action - (now - last_t), 1)
                status_msg = f"[Cooldown] {current_gesture} ready in {remaining}s"

        # ----------------------------------------------------
        # Render Premium HUD Overlay
        # ----------------------------------------------------
        # Top Header Bar
        cv2.rectangle(frame, (0, 0), (w, 60), (20, 20, 25), -1)

        # App Title
        cv2.putText(frame, "HAND TRACKING GESTURE APP LAUNCHER", (15, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, "✌️ YouTube | ☝️ ChatGPT | 🤘 Instagram | 3️⃣ Antigravity | 🤙 Task Manager", (15, 48),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (180, 180, 180), 1)

        # Current Gesture Display Panel (Top Left Overlay)
        cv2.rectangle(frame, (15, 75), (320, 135), (35, 35, 40), -1)
        cv2.rectangle(frame, (15, 75), (320, 135), (70, 70, 80), 1)

        cv2.putText(frame, "DETECTED GESTURE:", (25, 93),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (180, 180, 180), 1)

        g_colors = {
            "PEACE": (255, 215, 0),
            "POINTER": (0, 255, 255),
            "ROCK": (255, 20, 147),
            "THREE_FINGERS": (138, 43, 226),
            "PINKY_ONLY": (0, 255, 127),
            "NONE": (120, 120, 120)
        }
        disp_color = g_colors.get(current_gesture, (255, 255, 255))
        cv2.putText(frame, current_gesture, (25, 122),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, disp_color, 2)

        # Action Alert Banner (Center Screen Overlay)
        if now < action_banner_expire and action_banner:
            cv2.rectangle(frame, (30, h // 2 - 35), (w - 30, h // 2 + 25), (10, 10, 15), -1)
            cv2.rectangle(frame, (30, h // 2 - 35), (w - 30, h // 2 + 25), action_banner_color, 2)
            cv2.putText(frame, action_banner, (45, h // 2 + 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, action_banner_color, 2)

        # Bottom Status Log Bar
        cv2.rectangle(frame, (0, h - 35), (w, h), (15, 15, 20), -1)
        cv2.putText(frame, status_msg, (15, h - 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (220, 220, 220), 1)

        # Keyboard Controls Legend
        cv2.putText(frame, "Press 'Q' or 'ESC' to Exit", (w - 200, h - 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (140, 140, 140), 1)

        # Display camera feed window
        cv2.imshow("Hand Tracking Gesture Controller", frame)

        # Handle Keyboard Inputs
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == ord('Q') or key == 27:
            print("[Info] Exit key pressed. Shutting down...")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("[Info] Cleanup completed successfully.")

if __name__ == "__main__":
    main()