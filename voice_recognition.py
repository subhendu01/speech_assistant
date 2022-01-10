import speech_recognition as sr
import wikipedia, datetime, pyttsx3, pyjokes, random, webbrowser, os

# voice setting
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice',  voices[1].id)
engine.setProperty('voice', 'english+f2')
engine.setProperty('rate', rate - 70)

def speak(txt_input):
    engine.say(txt_input)
    engine.runAndWait()

def inputs():
    r = sr.Recognizer()
    r.pause_threshold = 1
    count = 0
    while True:
        with sr.Microphone() as source:
            print("Alexa: Listening...")
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio, language='en-ln')
                print(f"User:{query}")
                # speak('User ' + query)
                return query
                break
            except:
                count += 1
                if count > 3:
                    break
                print("Try Again")

def greetings():
    time_h = datetime.datetime.now().hour
    if time_h>=5 and time_h<12:
        speak('Good Morning!')
    elif time_h>=12 and time_h<17:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am bugs. How Can I help you?')

def random_qn():
    qns = ['Sing me a song', 'Tell me a story', 'I am said, what should I do.']
    speak(random.choice(qns))

if __name__ == "__main__":
    greetings()
    while True:
        query = inputs().lower()
        if 'hello' in query:
            speak("Hello! My  Name is bugs")
        elif 'name' in query:
            speak("My  Name is bugs")
        elif 'are you free' in query:
            answers = ['I am always free for my master', 'No, I am very expensive!']
            speak(random.choice(answers))
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"It is {time} Sir")
        elif 'music' in query:
            speak(f"playing music")
            os.system('xdg-open add_your_file_path')
        elif 'shutdown' in query:
            speak('Shutting down your system')
            os.system("shutdown /s")
        elif 'who is' in query:
            query = query.replace('who is', "")
            speak('According to wikipedia ')
            results = wikipedia.summary(query, 2)
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open('https://www.google.com')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'joke' in query:
            results = pyjokes.get_joke()
            print(results)
            speak(results)
        elif "bye" in query:
            speak("Have a nice day ! ")
            break
        else:
            ans = ["I don't understand what you are saying", "I'm Sorry Can you repeat again", "I think i miss that"]
            speak(random.choice(ans))
