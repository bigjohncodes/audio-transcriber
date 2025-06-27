import os
import yt_dlp
import whisper
from tqdm import tqdm

# Define working folders
folder_audio = "audios"
folder_transcriptions = "transcriptions"
url_file = "vimeo.txt"

# Create folders if they don't exist
os.makedirs(folder_audio, exist_ok=True)
os.makedirs(folder_transcriptions, exist_ok=True)

# Load the Whisper model
model = whisper.load_model("base")

def download_audio_vimeo(url, output_path):
    """Download only the audio from the Vimeo video and save it to the specified location."""
    options = {
        "format": "bestaudio",
        "outtmpl": output_path,
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}]
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

def transcribe_audio(audio_path, output_text_path):
    """Transcribe the audio and save segmented transcription with timestamps."""
    result = model.transcribe(audio_path)
    
    with open(output_text_path, "w", encoding="utf-8") as text_file:
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()
            # Write each segment on a new line with timestamps
            text_file.write(f"[{start:.2f}s --> {end:.2f}s] {text}\n")

def process_urls():
    """Read URLs, download audio, transcribe it, then delete the audio file."""
    with open(url_file, "r") as f:
        urls = [line.strip() for line in f.readlines() if line.strip()]

    for url in tqdm(urls):
        print(f"\n🔽 Processing: {url}")

        # Determine output audio filename
        output_audio_path = os.path.join(folder_audio, "%(title)s.%(ext)s")
        download_audio_vimeo(url, output_audio_path)

        # Find the downloaded audio file
        mp3_files = [f for f in os.listdir(folder_audio) if f.endswith(".mp3")]
        if not mp3_files:
            print(f"⚠️ No downloaded file found for {url}")
            continue

        audio_file = os.path.join(folder_audio, mp3_files[0])
        output_text_path = os.path.join(folder_transcriptions, f"{os.path.splitext(mp3_files[0])[0]}.txt")

        # Transcribe and delete audio file
        transcribe_audio(audio_file, output_text_path)
        os.remove(audio_file)
        print(f"✅ Transcription saved and audio deleted: {output_text_path}")

if __name__ == "__main__":
    process_urls()
