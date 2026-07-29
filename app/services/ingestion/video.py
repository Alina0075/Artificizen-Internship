from moviepy import VideoFileClip
import whisper

model = whisper.load_model("base")
def extract_video(file_path: str):
    clip=VideoFileClip(file_path)
    audio_path="temp_audio.wav"
    clip.audio.write_audiofile(audio_path)
    result=model.transcribe(audio_path)
    return [result["text"]]
