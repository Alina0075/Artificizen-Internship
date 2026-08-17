import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def extract_audio(file_path: str):
    with open(file_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            response_format="json"
        )

    return [transcription.text]