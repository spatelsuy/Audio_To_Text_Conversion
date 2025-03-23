import whisper
import ffmpeg
import argparse
import os

def transcribe_audio(audio_path):
    # Load the Whisper model
    model = whisper.load_model("base")  # You can use 'base', 'small', 'medium', or 'large'

    # Convert the audio to WAV format (if needed)
    converted_audio = "converted_audio.wav"
    ffmpeg.input(audio_path).output(converted_audio).run(overwrite_output=True)

    # Transcribe the audio
    result = model.transcribe(converted_audio)

    # Print and save the transcribed text
    print("Transcribed Text: ", result["text"])
    
    # Save output to a text file
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
