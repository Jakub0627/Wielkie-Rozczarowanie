import tkinter as tk
from tkinter import filedialog, messagebox
import os
from video_recognition import find_slide_changes_and_save_frames, create_pptx_with_frames, cut_video_segments
from audio_recognition import convert_to_wav, recognize_speech_from_audio_file


class VideoAudioRecognitionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video and Audio Recognition")
        self.geometry("800x600")
        self.init_ui()

    def init_ui(self):
        self.open_file_btn = tk.Button(self, text="Wybierz plik wideo", command=self.open_and_process_file)
        self.open_file_btn.pack(pady=20)

        self.status_area = tk.Text(self, height=15, width=95)
        self.status_area.pack(pady=10)

    def open_and_process_file(self):
        file_path = filedialog.askopenfilename(filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))
        if file_path:
            try:
                base_name = os.path.basename(file_path)
                name_without_ext = os.path.splitext(base_name)[0]
                output_dir = os.path.join(os.getcwd(), name_without_ext + "_output")
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                self.update_status("Processing video for slide changes...")
                timestamps, frame_paths = find_slide_changes_and_save_frames(file_path)
                pptx_path = os.path.join(output_dir, f"{name_without_ext}.pptx")
                create_pptx_with_frames(frame_paths, pptx_path)
                self.update_status("PowerPoint presentation created.")

                self.update_status("Processing audio for the full video...")
                self.process_audio(file_path, output_dir, "full_video")

                self.process_video_segments(file_path, timestamps, output_dir)

                self.update_status("All processing complete. Check the output folder.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def process_video_segments(self, video_path, timestamps, output_dir):
        # Create "cuts" folder inside the output directory
        cuts_output_folder = os.path.join(output_dir, "cuts")
        if not os.path.exists(cuts_output_folder):
            os.makedirs(cuts_output_folder)

        if len(timestamps) > 0:
            cut_video_segments(video_path, timestamps, cuts_output_folder)
            self.update_status("Video segments created.")

            for i in range(len(timestamps)):
                segment_path = os.path.join(cuts_output_folder, f'segment_{i}.mp4')
                if os.path.exists(segment_path):
                    self.update_status(f"Processing audio for segment: segment_{i}.mp4...")
                    self.process_audio(segment_path, cuts_output_folder, f"segment_{i}")
                else:
                    self.update_status(f"Skipped processing for non-existent segment: segment_{i}.mp4")
        else:
            self.update_status("No segments were found to process.")

    def process_audio(self, video_path, output_dir, prefix):
        wav_path = os.path.join(output_dir, f"{prefix}.wav")
        convert_to_wav(video_path, wav_path)
        transcript = recognize_speech_from_audio_file(wav_path)
        with open(os.path.join(output_dir, f"{prefix}_transcript.txt"), "w", encoding="utf-8") as f:
            f.write(transcript)

    def update_status(self, message):
        self.status_area.insert(tk.END, message + "\n")
        self.status_area.see(tk.END)
        self.update()

if __name__ == "__main__":
    app = VideoAudioRecognitionApp()
    app.mainloop()
