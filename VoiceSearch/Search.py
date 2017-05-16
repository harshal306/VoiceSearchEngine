# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:22:47 2017

@author: harshal mittal
"""
import speech_recognition as sr
import pyttsx as pt
import wikipedia
import webbrowser
from google import search

r = sr.Recognizer()
engine = pt.init()

engine.say("Ask me something!!!!")
engine.runAndWait()
print ("Ask me Something!!!")
    
with sr.Microphone() as source:
    audio = (r.listen(source))
    
audio = r.recognize_google(audio)
try:
    print ("Initializing...")
    engine.say("Ok, Searching wikipedia for "+audio)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


try:
    srch = wikipedia.summary(audio,sentences = 2)
    print (srch)
    engine.say(srch)
    engine.runAndWait()
    engine.say("If you want more information, I can search on google as well. Do you want me to search on google?")
    engine.runAndWait()
    print ("Give answer!!")
    with sr.Microphone() as source:
        choice = r.listen(source)
    choice = r.recognize_google(choice)
    print (choice+" Got it!!")
    if (choice == "yes" or choice == "ok" or choice == "sure"):
        engine.say("Great!, Allow me to open web browser for you!")
        engine.runAndWait()
        #no_of_search = search(audio, tld='com.pk', lang='es', stop=5)
        for url in search(audio, tld='com.pk', lang='es', stop=5):
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)
            break
    else:
        engine.say("Ok! No problem!!")
        engine.runAndWait()
except Exception:
    engine.say("There are many things that are related to "+audio+", Kindly Specify which "+audio)
    engine.runAndWait()

