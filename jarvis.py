import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')

#print(voices[1].id)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if(hour>=0 and hour<12):
        speak("Good morning")

    elif(hour>=12 and hour<18):
        speak('Good Afternoon')

    else:
        speak("Good Evening")

    speak("HI,MY NAME IS JARVIS. HOW CAN I HELP YOU")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio,language='en-us')
            print(f'User Said: {query}')

        except Exception as e:

            speak('Sorry,I couldnt recognize what you said')
            query = takeCommand().lower()
            return query

        return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jethababita1970@gmail.com','jethalovesbabita')
    server.sendmail('jethababita1970@gmail.com',to,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'your name' in query: 
            speak('I am Jarvis')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir the time is {strTime}')

        elif 'open telegram' in query:
            codePath = "C:\\Users\\HIMANSHUU\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(codePath)

        elif 'play a song' in query:
            music_dir = "C:\\Users\\HIMANSHUU\\Downloads\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randrange(0,5)]))

        elif 'add' in  query:
            speak('Tell me first Number: ')
            num1 = float(input("Enter first no: "))
            speak('Tell me second Number: ')
            num2 = float(input("Enter first no: "))
            print(f'Sum = {num1+num2}')
            speak(f'The addition of {num1} and {num2} is {num1 + num2}')

        elif 'email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "himanshubobade007@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry wasnt able to send email")
            
