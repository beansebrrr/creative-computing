"""
Text to Speech using pyttsx3
"""

import pyttsx3 as tts
import datetime


engine = tts.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    speak("Hello!")
    if hour in range(4, 12):
        speak("Good morning!")
    elif hour in range(12, 16):
        speak("Good afternoon.")
    elif hour in range(16, 20):
        speak("Good evening.")
    else:
        speak("Go to sleep bruv")
        return
    

greet()