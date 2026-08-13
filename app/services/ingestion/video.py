import os
import whisper
from moviepy import VideoFileClip

model = whisper.load_model("base")

def extract_video(file_path: str):
    audio_path = file_path + "_audio.wav"
    clip = VideoFileClip(file_path)
    clip.audio.write_audiofile(audio_path, logger=None)
    clip.close()

    result = model.transcribe(audio_path)

    os.remove(audio_path)
    return [result["text"]]