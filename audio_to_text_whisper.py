import whisper
import subprocess
import argparse
import os

ALLOWED_EXTENSIONS = (".mp3", ".mp4", ".wav", ".flac")

def transcribe_audio(audio_path):
    if not audio_path.lower().endswith(ALLOWED_EXTENSIONS):
        print("Error: Unsupported audio format. Use MP3, MP4, WAV, or FLAC.")
        return

    model = whisper.load_model("base")

    # Convert audio to WAV if not already in WAV format
    converted_audio = "converted_audio.wav"
    if not audio_path.lower().endswith(".wav"):
        subprocess.run(["ffmpeg", "-i", audio_path, "-ar", "16000", "-ac", "1", "-y", converted_audio])
    else:
        converted_audio = audio_path

    result = model.transcribe(converted_audio)

    print("\nTranscribed Text: ", result["text"])

    with open("transcription.txt", "w", encoding="utf-8") as file:
        file.write(result["text"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert audio to text using Whisper.")
    parser.add_argument("audio_file", type=str, help="Path to the input audio file")
    args = parser.parse_args()

    if not os.path.exists(args.audio_file):
        print("Error: File does not exist!")
    else:
        transcribe_audio(args.audio_file)
