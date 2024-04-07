# Wielkie-Rozczarowanie

## Overview
Hackcarpathia

<!DOCTYPE html>
<html>
<body>
  
  <iframe src="[url video in google drive/preview](https://drive.google.com/file/d/1EKkZkYA_v2MM8JoqV5MYg5IBGfFCT54T/view?usp=drive_link)](https://drive.google.com/file/d/1EKkZkYA_v2MM8JoqV5MYg5IBGfFCT54T/view)" ></iframe>
  
  <!--aloow full screen add tag -->
  
<iframe allowfullscreen="allowfullscreen" src="your_page_url/preview" ></iframe>

</body>
</html>


Flex your gray matter and show that you're able to overcome our challenges.

This project aims to enable students or lecturers to create transcripts from online lectures. It converts presentations shown during classes into PowerPoint (PPTX) files and generates a full audio transcript of the lecture. The primary goal is to facilitate access to educational materials for people who are deaf or hard of hearing, thereby reducing educational inequalities.

## Files

### main.py
This program is a GUI application that processes video and audio files. It extracts slides from the video, creates a PowerPoint presentation, cuts the video into segments, and transcribes the audio into text files.

### audio_recognition.py
This script provides functions for converting audio files to WAV format and performing speech recognition on them using the Google Speech Recognition API.

#### Functions:
- **convert_to_wav**: Converts an audio file to WAV format.
- **recognize_speech_from_audio_file**: Recognizes speech from an audio file.

### video_recognition.py
The program is designed to process video files, detect major slide changes within them, create a PowerPoint presentation from the detected frames, and cut the video into segments based on those changes.

#### Functions:
- **find_slide_changes_and_save_frames**: Detects major slide changes in a video and saves the frames before each change.
- **create_pptx_with_frames**: Creates a PowerPoint presentation with each saved frame as a slide.
- **cut_video_segments**: Cuts the video into segments based on specified timestamps and saves them to a folder.
