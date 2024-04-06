# Wielkie-Rozczarowanie
Hackcarpathia

Flex your gray matter and show that you're able to overcome our challenges.

This project is a software aimed at enabling students or lecturers to create transcripts from online lectures. It converts presentations shown during classes into pptx files and generates a full audio transcript of the lecture. The main goal of this project is to facilitate access to educational materials for people who are deaf or hard of hearing, thereby reducing educational inequalities.


main.py

  This program is a GUI application that processes video and audio files. It extracts slides from the video, creates a PowerPoint presentation, cuts the video into segments, and transcribes the audio into text files.

audio_recogniction.py

  This script provides functions for converting audio files to WAV format and performing speech recognition on them using the Google Speech Recognition API.
  There are 2 functions in this file:
  
    convert_to_wav: Converts an audio file to WAV format.

    recognize_speech_from_audio_file: Recognizes speech from an audio file.

video_recognition.py

  The program is designed to process video files, detect major slide changes within them, create a PowerPoint presentation from the detected frames, and cut the video into segments based on those changes.
  There are 3 functions in this file:
  
    find_slide_changes_and_save_frames: Detects major slide changes in a video and saves the frames before each change.

    create_pptx_with_frames: Creates a PowerPoint presentation with each saved frame as a slide.

    cut_video_segments: Cuts the video into segments based on specified timestamps and saves them to a folder.


