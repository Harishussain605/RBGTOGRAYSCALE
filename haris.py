from gtts import gTTS
from playsound import playsound
import os
def speak(textToSpeak):
    myobj = gTTS(text=textToSpeak, lang='en')
    myobj.save("voices\convertedText.mp3")
    playsound("voices\convertedText.mp3")
    os.remove("voices\convertedText.mp3")

mytext= 'hello syed haris '
speak(mytext)