def add_audio_to_video(video_file, audio_file, output_file):
    from moviepy.editor import VideoFileClip, AudioFileClip

    # Load the video and audio files
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)

    # Trim the audio to match the video's duration
    # If the audio is shorter than the video, this will use the full audio.
    # If the audio is longer, it will be cut to the video's length.
    trimmed_audio = audio.subclip(0, video.duration)

    # Set the (trimmed) audio of the video
    # The video object retains its original duration.
    # Setting an audio track that is shorter or equal in duration will not change the video's duration.
    final_video = video.set_audio(trimmed_audio)

    # Write the result to a new file
    # The duration of final_video will be determined by the original video's duration.
    final_video.write_videofile(output_file, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    video_path = r"C:\Users\nitro\OneDrive\Videos\2025-06-07 12-54-57.mkv"
    audio_path = r"C:\Users\nitro\OneDrive\Videos\Music\Favorite Library No Copyright Lofi Hip Hop & Chillhop 407.mp4"  # Replace with your audio file path
    output_path = r"C:\Users\nitro\OneDrive\Videos\2025-6-07-001-_video_with_audio.mp4"  # Desired output path

    add_audio_to_video(video_path, audio_path, output_path)