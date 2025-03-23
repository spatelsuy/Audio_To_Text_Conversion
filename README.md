# Audio to Text Conversion using Whisper on Windows

This guide explains the steps to set up a **Python environment** on **Windows** for converting audio to text using **Whisper** and **FFmpeg**.

## Prerequisites
- Python 3.x
- FFmpeg (for audio conversion)
- Whisper (for speech-to-text)

## Python Libraries:
- openai-whisper (for transcription)
- ffmpeg-python (or subprocess for FFmpeg execution)
- argparse (for command-line input handling)

## Step 1: Install Python and verify

**Download Python** from the official website:  [Python Downloads](https://www.python.org/downloads/)  
Run the installer.  
Make sure to **check the box that says "Add Python to PATH"** before clicking **Install Now**.  

On **Command Prompt** run following command. You should see the Python version.:  
```cmd
python --version
```

## Step 2: Setup and activate virtual environment

**Create a Virtual Environment**:
Navigate to your project directory (where you want to store your project).
```cmd
python -m venv audio_to_text
.\audio_to_text\Scripts\activate
```
You should see `(audio_to_text)` at the beginning of the command prompt indicating the virtual environment is active.

## Step 3: Install required libraries

**Install torch openai-whisper ffmpeg-python**:
With the virtual environment activated, run:
```cmd
pip install torch openai-whisper ffmpeg-python
```

## Step 4: Install FFmpeg  
Go to the FFmpeg official website to download it:  [FFmpeg Download](https://ffmpeg.org/download.html)  
Download the **Windows builds from Gyan**:  [FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/)  
Download the **Release build** zip file.  
Extract it (e.g., to `C:\ffmpeg`) and set environment PATH to FFmpeg's **bin** folder (e.g., `C:\ffmpeg\bin`).  

Verify FFmpeg Installation
```cmd
ffmpeg -version
```

## Step 5: Create Your Python Script for Audio-to-Text

1. **Create a Python file** (`audio_to_text_Whisper.py`) in your project directory.
   
2. **Add the following Python script**:

```python
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

```

## Step 6: Test it
An input file "input.mp3" has been provided to test. 
```
python audio_to_text_whisper.py input.mp3
```
## Output
The output looks like this:  
Transcribed Text:   In recent times, scammers and hackers have been approaching ordinary citizens, falsely claiming to represent the comment agencies. To protect the public from failing prey to such fraud, it would be beneficial for the comment to include a QR code-based system. In this approach, each legitimate comment officer could be assigned a unique QR code. The general public would then be able to scan the code to verify whether the person is genuine, confirm the legitimacy of the reported issues, and validate the authenticity of any request or demand made. This QR code system would provide a quick and easy way for citizens to differentiate between real government officials and scammers, ensuring greater transparency and security for the public.  


