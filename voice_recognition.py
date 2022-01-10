import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
import pyttsx3

# voice setting
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(txt_input):
    engine.say(txt_input)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    count = 0
    while True:
        with sr.Microphone() as source:
            print("Alexa: Listening...")
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio)
                print(f"master:{query}")
                speak('you said ' + query)
                return query
                break
            except:
                count += 1
                if count > 3:
                    break
                print("Try Again")

while True:
    query = command().lower()  ## takes user command
    if 'name' in query:
        speak("Hello Machine! My  Name is Alexa")
    elif 'are you single' in query:
        answers = ['I am in a relationship with wifi', 'No, I love spending time thinking about my crush wifi']
        speak(random.choice(answers))
    elif 'hate' in query:
        speak("I hate when people called me a machine")
    elif 'love' in query:
        speak("I loves to chat with machines like you")
    ### time
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("It's {time} master")

    ### celebrity
    elif 'who is' in query:
        query = query.replace('who is', "")
        speak(wikipedia.summary(query, 2))

    ### Joke
    elif 'joke' in query:
        speak(pyjokes.get_joke())


    elif "bye" in query:
        speak("Have a nice day ! ")
        break
    else:
        speak("I don't understand what you are saying")