from faster_whisper import WhisperModel
import os
def transcribe_model(file_path):
    print("⏳ Loading Faster-Whisper model...")
    cache_path = os.path.join(os.path.dirname(__file__), "whisper_cache")
    os.makedirs(cache_path, exist_ok=True)
    model_size = "base"  # use "tiny" for speed, "small" for more accuracy
    model = WhisperModel(
        model_size,
        compute_type="int8",           # perfect for CPU-only systems
        download_root=cache_path       # local cache folder
    )
    print("🎧 Transcribing audio...")
    segments, _ = model.transcribe(file_path)
    full_text = " ".join([segment.text for segment in segments])
    print("✅ Transcription complete.")
    return full_text
if __name__ == "__main__":
    test_file = os.path.join(os.path.dirname(__file__), "..", "test_audio.m4a")  
    try:
        output = transcribe_model(test_file)
        print("\n📝 Transcription:\n")
        print(output)
    except FileNotFoundError:
        print(f"❌ File '{test_file}' not found. Make sure it's in the correct folder.")
    except Exception as e:
        print(f"🚨 Error during transcription: {str(e)}")
