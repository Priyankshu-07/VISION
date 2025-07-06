import os
import uuid
from yt_dlp import YoutubeDL
from models.whisper_model import transcribe_model
def transcribe_youtube(url: str) -> str:
    try:
        print(f"📥 Downloading audio using yt-dlp: {url}")
        output_dir = "downloads"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        file_basename = str(uuid.uuid4())
        output_template = os.path.join(output_dir, f"{file_basename}.%(ext)s")
        final_path = os.path.join(output_dir, f"{file_basename}.mp3")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        if not os.path.exists(final_path):
            raise Exception("Downloaded audio file not found. Something went wrong.")
        print(f"🎧 Audio downloaded: {final_path}")
        transcription = transcribe_model(final_path)
        print("✅ Transcription complete.")
        os.remove(final_path)
        return transcription
    except Exception as e:
        print(f"❌ Error: {e}")
        raise Exception(f"YouTube transcription failed: {str(e)}")
