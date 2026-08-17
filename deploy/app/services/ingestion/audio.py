import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_audio(file_path: str):
    with open(file_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=f,
            response_format="text"
        )
    return [transcription]