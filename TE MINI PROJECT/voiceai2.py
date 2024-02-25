# ctrl + shift + p ---> to select interpreter
from time import ctime
import speech_recognition as sr
import webbrowser
from gtts import gTTS
import os
import playsound
import random
import time

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            martin_speak(ask)
        audio = r.listen(source)
        voice_data= ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            martin_speak('Sorry, I did not get that')
        except sr.RequestError:
            martin_speak('Sorry, my speech service is down')

        return voice_data

def martin_speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'your name' in voice_data:
        martin_speak('My name is lynda')

    if 'time' in voice_data:
        martin_speak(ctime())

    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        martin_speak('Here is what i found for '+ search)

    if 'location' in voice_data:
        location = record_audio('What location do you want me to tell your location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        martin_speak('Here is your location '+ location)

    if 'exit' in voice_data:
        exit()

time.sleep(1)
martin_speak('How can I help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)