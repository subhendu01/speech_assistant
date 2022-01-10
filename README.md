# speech_recognition
Speech Recognition using python

First install the below libraries:
1. pip install pyttsx3
2. pip install SpeechRecognition

If you found the below error 
- “OSError: libespeak.so.1: cannot open shared object file: No such file or directory site:stackoverflow.com” Code Answer’s
<br/>
It's because you don't have espeak installed on your system. That's why it is giving error

  1. sudo apt-get update && sudo apt-get install espeak