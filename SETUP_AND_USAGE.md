# Speech to Text Application

A simple Python application that captures audio from your microphone and converts it to text using Google Speech Recognition.

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. System Dependencies

You may need to install audio libraries depending on your OS:

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-pyaudio
# or
sudo apt install portaudio19-dev
pip install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Windows:**
PyAudio is included in the pip package, but you may need the Visual C++ Build Tools installed.

## Usage

Run the script:

```bash
python speech_to_text.py
```

The program will:
1. Start listening through your microphone
2. Wait for you to speak
3. Automatically stop listening after a period of silence (typically 2-3 seconds)
4. Convert your speech to text using Google's API
5. Display the recognized text

## Features

- **Simple Interface**: Just run the script and start speaking
- **Free**: Uses Google Speech Recognition API (no API key needed)
- **Error Handling**: Handles connection errors and unrecognized speech gracefully
- **Timeout Protection**: Automatically times out to prevent hanging

## Troubleshooting

- **"No audio input device found"**: Make sure you have a working microphone connected
- **"Could not understand audio"**: Speak clearly and try again
- **"Error connecting to service"**: Check your internet connection (Google API requires internet)
- **Audio not being captured**: Check microphone permissions and volume levels

## Alternative: Offline Speech Recognition

For offline use without internet dependency, you can modify the script to use Pocketsphinx:

```bash
pip install pocketsphinx
```

Then replace the `recognize_google()` call with `recognize_sphinx()`.
