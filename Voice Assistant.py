#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak('Good Morning!')
    elif hour<=12 and hour<15:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak("I am Siri! How can I assist you today?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        audio = r.listen(source)
        
    try:
        print('recognizing..')
        query = r.recognizing_bing(audio,language='en-US')
        print(f"user said:{query}\n")
        
    except Exception as e:
        print("Could you please sasy that again?")
        return "None"
    return query

if __name__=="__main__":
    greet()
    while True:
        query = command().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query,lines=2)
            speak('According to Wikipedia')
            print(result)
            speak(result)
            
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"It's{time}")
            
        elif 'quit' in query:
            speak("Thank you! Have a great day!")
            exit()


# In[ ]:





# In[ ]:




