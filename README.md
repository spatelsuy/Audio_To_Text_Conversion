# Audio to Text Conversion with VOSK on Windows

This guide explains the steps to set up a **Python environment** on **Windows** for converting audio to text using **VOSK** and **FFmpeg**.

## Prerequisites
- Python 3.x
- FFmpeg (for audio conversion)
- VOSK (for speech-to-text)

### Step 1: Install Python

1. **Download Python** from the official website:  [Python Downloads](https://www.python.org/downloads/)  
Run the installer.  
Make sure to **check the box that says "Add Python to PATH"** before clicking **Install Now**.  

3. **Verify Installation**:  
On **Command Prompt** run following command. You should see the Python version.:  
```cmd
python --version
```
### Step 2: Set Up a Virtual Environment

1. **Create a Virtual Environment**:
Navigate to your project directory (where you want to store your project).
```cmd
python -m venv audio_to_text
```

2. **Activate the Virtual Environment**:
```cmd
.\audio_to_text\Scripts\activate
```
You should see `(audio_to_text)` at the beginning of the command prompt indicating the virtual environment is active.

### Step 3: Install Required Libraries

1. **Install Vosk and Wave**:
With the virtual environment activated, run:
```cmd
pip install vosk wave
```

2. **Install FFmpeg**:
Go to the FFmpeg official website to download it:  
[FFmpeg Download](https://ffmpeg.org/download.html)
Download the **Windows builds from Gyan**:  
[FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/)  
Download the **Release build** zip file.  
Extract it (e.g., to `C:\ffmpeg`).  
Add the path to FFmpeg's **bin** folder (e.g., `C:\ffmpeg\bin`).  
Verify FFmpeg Installation
```cmd
ffmpeg -version
```

### Step 4: Download the Vosk Model

1. Download a pre-trained model from the [Vosk Models page](https://alphacephei.com/vosk/models).
2. For example, download the **vosk-model-en-us-0.22.zip** for English.
3. Extract the model to a folder (e.g., `C:\vosk_model`).

### Step 5: Create Your Python Script for Audio-to-Text

1. **Create a Python file** (`audio_to_text_Vosk.py`) in your project directory.
   
2. **Add the following Python script**:

```python
import wave
import json
import subprocess
from vosk import Model, KaldiRecognizer

# Convert any audio to WAV using FFmpeg
def convert_to_wav(input_file, output_file="converted_audio.wav"):
    command = ["ffmpeg", "-i", input_file, "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", output_file, "-y"]
    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output_file

# Transcribe WAV using VOSK
def transcribe_audio(wav_file, model_path="C:/vosk_model"):
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)

    with wave.open(wav_file, "rb") as wf:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            recognizer.AcceptWaveform(data)

    result = json.loads(recognizer.FinalResult())
    return result.get("text", "")

# Run the process
audio_file = "sample.mp3"  # Replace with your audio file
wav_file = convert_to_wav(audio_file)
text = transcribe_audio(wav_file)
print("Transcribed Text:", text)
