import os
from moviepy import VideoFileClip
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_video(file_path: str):
    audio_path = file_path + "_audio.wav"
    clip = VideoFileClip(file_path)
    clip.audio.write_audiofile(audio_path, logger=None)
    clip.close()

    with open(audio_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=f,
            response_format="text"
        )

    os.remove(audio_path)   
    return [transcription]