import speech_recognition as sr

def speech_to_text():
    """
    Capture audio from microphone and convert to text.
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening... Please speak into the microphone.")
        print("(Listening will timeout after 10 seconds of silence)")
        
        try:
            # Listen to the microphone with a timeout
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=None)
            
            print("Processing audio...")
            
            # Use Google Speech Recognition API (free, no key required)
            text = recognizer.recognize_google(audio)
            
            print(f"Recognized text: {text}")
            return text
            
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error connecting to the speech recognition service: {e}")
            return None
        except sr.Timeout:
            print("Listening timed out. Please try again.")
            return None

if __name__ == "__main__":
    speech_to_text()
