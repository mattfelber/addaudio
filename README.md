# AddAudio: Simple Video Sound Merger

This app takes a video file and an audio file (like music) and combines them into a new video that has the original visuals with the new audio track.

## What it does

- **Adds audio to any video:** Perfect for adding background music, narration, or sound effects to silent videos
- **Automatic trimming:** If your audio track is longer than the video, it automatically cuts it to fit perfectly
- **Preserves video quality:** The video quality stays the same while the audio gets replaced

## When would you use this?

- Adding background music to videos
- Adding commentary to gameplay recordings
- Creating videos with custom soundtracks
- Replacing poor quality audio with better audio
- Replacing copyrighted music with royalty free

## Prerequisites

1. **Python 3.10 Interpreter**:
   The script requires Python 3.10. If you don't have it installed, download it from [python.org](https://www.python.org/downloads/release/python-3100/).

2. **MoviePy Library**:
   The script uses the MoviePy library. To install it:
   - Open Command Prompt (search for "cmd" in the Windows start menu)
   - Type this command and press Enter:
     ```
     pip install moviepy==1.0.3
     ```

## How to Use the App (Step-by-Step)

### Step 1: Edit the File Paths (Super Easy!)

1. **Find the Script File**:
   - Navigate to the `src` folder in this project
   - Open the file named `add_audio.py` in any text editor (like Notepad)
   - Scroll down to the bottom of the file

2. **Look for These Lines**:
   ```python
   if __name__ == "__main__":
       video_path = r"C:\Users\nitro\OneDrive\Videos\2025-06-07 12-54-57.mkv"
       audio_path = r"C:\Users\nitro\OneDrive\Videos\Music\Favorite Library No Copyright Lofi Hip Hop & Chillhop 407.mp4"
       output_path = r"C:\Users\nitro\OneDrive\Videos\2025-6-07-001-_video_with_audio.mp4"
   ```

3. **Change the Paths**:
   - **For the video file**: Replace the text between the quotes after `video_path =` with the location of your video file
   - **For the audio file**: Replace the text between the quotes after `audio_path =` with the location of your audio file
   - **For the output file**: Replace the text between the quotes after `output_path =` with where you want to save the new video

   **Important Tips**:
   - Keep the `r"` at the beginning of each path
   - Use the full path (like `C:\Users\YourName\Videos\my_video.mp4`)
   - Make sure to include the file extension (like `.mp4`, `.mkv`, etc.)
   - Don't remove any quotes or other characters

4. **Example**:
   ```python
   if __name__ == "__main__":
       video_path = r"C:\Users\John\Videos\my_vacation_video.mp4"
       audio_path = r"C:\Users\John\Music\favorite_song.mp3"
       output_path = r"C:\Users\John\Videos\vacation_with_music.mp4"
   ```

5. **How to Get the Full Path**:
   - In Windows File Explorer, navigate to your file
   - Right-click on the file and select "Properties"
   - Copy the "Location" path and add the filename at the end
   - Or, hold Shift, right-click the file and choose "Copy as path" (then remove the quotes when pasting)

### Step 2: Run the Script

1. Open Command Prompt (search for "cmd" in the Windows start menu)
2. Navigate to the script location by typing:
   ```
   cd path\to\addaudio\src
   ```
3. Run the script:
   ```
   python add_audio.py
   ```
4. Wait for the processing to complete (this may take a few minutes depending on your video size)
5. Check the output location for your new video!

## Troubleshooting

- **"File not found" error**: Double-check your file paths. Make sure the files exist at the locations you specified.
- **"Module not found" error**: Make sure you've installed the MoviePy library as described in the Prerequisites section.
- **Processing takes too long**: This is normal for larger video files. Be patient!

## Need Help?

If you encounter any issues, please open an issue on the GitHub repository.
