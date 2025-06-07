# Instructions for add_audio.py

This document provides step-by-step instructions to run the `add_audio.py` script located in the `src` directory. This script adds an audio track to a video file, trimming the audio to match the video's duration.

## Prerequisites

1.  **Python 3.10 Interpreter**:
    The script must be run with a specific Python 3.10 interpreter. The one confirmed to work is located at:
    `C:\Users\nitro\AppData\Local\Programs\Python\Python310\python.exe`

2.  **`moviepy` Library**:
    The `moviepy` library (version 1.0.3) must be installed for the Python interpreter mentioned above.
    *   **To check if installed or to install/reinstall:** Open PowerShell or Command Prompt and run:
        ```powershell
        C:\Users\nitro\AppData\Local\Programs\Python\Python310\python.exe -m pip install --no-cache-dir moviepy==1.0.3
        ```
    *   If you previously faced `ModuleNotFoundError`, ensure `pip` and `setuptools` are upgraded for this interpreter:
        ```powershell
        C:\Users\nitro\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip setuptools
        ```
        Then, try the `moviepy` installation command again.

## Running the Script

**Step 1: Modify File Paths in `add_audio.py` (Crucial!)**

Before running, you **must** update the hardcoded file paths within the `src/add_audio.py` script. Open this file in a text editor.

Find these lines near the end of the script:
```python
if __name__ == "__main__":
    video_path = r"C:\Users\nitro\OneDrive\Videos\2025-06-07 12-54-57.mkv"
    audio_path = r"C:\Users\nitro\OneDrive\Videos\Music\Favorite Library No Copyright Lofi Hip Hop & Chillhop 407.mp4"
    output_path = r"C:\Users\nitro\OneDrive\Videos\2025-6-07-001-_video_with_audio.mp4"

    add_audio_to_video(video_path, audio_path, output_path)
```
-   Change `video_path` to the full path of your input video file.
-   Change `audio_path` to the full path of your input audio file.
-   Change `output_path` to where you want the final video to be saved and what it should be named.

**Save the changes to `add_audio.py`.**

**Step 2: Open Terminal**

Open a Command Prompt or PowerShell window.

**Step 3: Navigate to the `src` Directory**

In the terminal, type the following command and press Enter:
```powershell
cd c:\Users\nitro\Documents\Werk\Code Drills\addaudio-python\src
```

**Step 4: Execute the Script**

In the terminal (which should now be in the `src` directory), type the following command and press Enter:
```powershell
C:\Users\nitro\AppData\Local\Programs\Python\Python310\python.exe add_audio.py
```

The script will process your video and audio files and save the output to the `output_path` you specified in the script. The terminal will show progress from `moviepy`.
