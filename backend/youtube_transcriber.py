import os
import uuid
from yt_dlp import YoutubeDL
from models.whisper_model import transcribe_model
def transcribe_youtube(url):
    print("Downloading audio from: " + url)
    if os.path.exists("downloads") == False:
        os.makedirs("downloads")
    random_name = str(uuid.uuid4())
    output_path = "downloads/" + random_name + ".%(ext)s"
    download_options = {}
    download_options['format'] = 'bestaudio/best'
    download_options['outtmpl'] = output_path
    download_options['quiet'] = True
    converter = {}
    converter['key'] = 'FFmpegExtractAudio'
    converter['preferredcodec'] = 'mp3'
    converter['preferredquality'] = '192'
    download_options['postprocessors'] = [converter]
    downloader = YoutubeDL(download_options)
    downloader.download([url])
    mp3_file = None
    files = os.listdir("downloads")
    for file in files:
        if ".mp3" in file:
            mp3_file = "downloads/" + file
            break   
    if mp3_file == None:
        print("Could not find downloaded audio file")
        return None   
    print("Audio downloaded")
    text = transcribe_model(mp3_file)
    print("Transcription done")
    os.remove(mp3_file)    
    return text