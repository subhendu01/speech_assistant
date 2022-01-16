# Speech Recognition using python

Here I've used some basic python libraries to build a voice assistance.

First install the below libraries:
      
     1. pip install SpeechRecognition
     2. pip install pyttsx3

SpeechRecognition: This Python library is used to convert speech into text <br/>
Pyttsx3: Pyttsx3 is a text to speech python library used to convert text into speech.

:point_right: Don't give the python file name as speech_recognition.py or else it may give you error.

## For voice configuration please visit the below website:
  
    https://pyttsx.readthedocs.io/en/latest/engine.html#changing-voices

### If you found the below error
 
“OSError: libespeak.so.1: cannot open shared object file: No such file or directory site:stackoverflow.com” Code Answer’s
<br/>
  
    It's because you don't have espeak installed on your system. That's why it is giving error
    1. sudo apt-get update && sudo apt-get install espeak

After installation run the voice_recognition.py file and enjoy with your assistance. :sweat_smile:
  
