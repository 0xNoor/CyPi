import speech_recognition as sr
import time
import sounddevice
import pyautogui

# Create a recognizer instance
r = sr.Recognizer()

# Specify the audio source (e.g., microphone or audio file)
# For microphone input, use sr.Microphone() as the source
# For audio file input, use sr.AudioFile('audio_file.wav') as the source
source = sr.Microphone(device_index=1)

# Adjust for ambient noise (optional)
# Uncomment the following line if you need to adjust for ambient noise
# with source as source:


print("Listening...")

with source as source:
    audio = r.listen(source, phrase_time_limit=5)

# Perform speech recognition
try:
    # Use the default API key for Google Speech Recognition
    text = r.recognize_google(audio)
    print("Recognized Text:")
    pyautogui.typewrite(text)
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")