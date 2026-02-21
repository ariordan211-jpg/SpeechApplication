from speech_to_text import speech_to_text
from llm_lmstudio import ask_llm
from tts_piper import speak

if __name__ == "__main__":
    # Set to True to bypass microphone for testing and use a hardcoded prompt
    TEST_BYPASS_STT = True

    if TEST_BYPASS_STT:
        text = "How are you"
        print("(TEST MODE) Using hardcoded prompt:", text)
    else:
        # Get speech -> text
        text = speech_to_text()

    if text:
        reply = ask_llm(text)
        if not reply:
            print("No reply from LM Studio.")
        else:
            # Speak the LM Studio reply using Piper
            speak(reply)
    else:
        print("No speech recognized to send to LM Studio.")
