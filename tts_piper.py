import subprocess
import os
import winsound

# Piper TTS configuration - update paths if needed
PIPER_EXE = r"C:\Users\anner\Downloads\piper_windows_amd64\piper\piper.exe"
PIPER_MODEL = r"C:\Users\anner\Downloads\piper_windows_amd64\en_GB-alba-medium.onnx"
RESPONSE_WAV = "response.wav"
# Path to ffplay; if ffplay is in PATH, leave as 'ffplay'
FFPLAY_PATH = r"C:\ffmpeg\bin\ffplay.exe"


def speak(text):

    if not text:
        return

    cmd = [
        PIPER_EXE,
        "--model", PIPER_MODEL,
        "--output_file", RESPONSE_WAV
    ]

    try:
        p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE
        )

        p.stdin.write(text.encode("utf-8"))
        p.stdin.close()
        p.wait()
    except Exception as e:
        print("❌ TTS Error:", e)
        return

    # Play the response WAV.
    # 1) Try configured ffplay path
    try:
        if os.path.exists(FFPLAY_PATH):
            subprocess.run([FFPLAY_PATH, "-autoexit", RESPONSE_WAV], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return

        # 2) Try `ffplay` from PATH
        try:
            subprocess.run(["ffplay", "-autoexit", RESPONSE_WAV], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return
        except FileNotFoundError:
            pass

        # 3) Fallback to Windows winsound (built-in)
        try:
            winsound.PlaySound(RESPONSE_WAV, winsound.SND_FILENAME)
            return
        except Exception as e:
            print("❌ Playback error (winsound):", e)
    except FileNotFoundError as e:
        print("❌ Playback error: ffplay not found -", e)
    except Exception as e:
        print("❌ Playback error:", e)
