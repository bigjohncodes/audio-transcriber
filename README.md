# 🎧 Video Audio Transcriber with OpenAI Whisper

This project allows you to **download audio from Vimeo videos**, **transcribe it using OpenAI’s Whisper model**, and **save the results as text files** — all in an automated workflow.

## 🚀 Features

- Download audio from Vimeo using `yt-dlp`
- Transcribe audio using OpenAI's Whisper model
- Save transcriptions to `.txt` files
- Clean up audio files after transcription
- Simple and extensible project structure

---

## 🧰 Requirements

Before running the script, make sure you have the following installed:

- Python 3.7 or higher
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [ffmpeg](https://ffmpeg.org)
- [tqdm](https://github.com/tqdm/tqdm)

### 🔧 Install Dependencies

```bash
pip install yt-dlp tqdm
pip install git+https://github.com/openai/whisper.git
