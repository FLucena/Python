# pyttsx3 - Text-to-speech - Only works in English
# https://pyttsx3.readthedocs.io/en/latest/engine.html

import pyttsx3
book = open(r"book.txt")
book_text = book.readlines()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
for i in book_text:
    engine.say(i)
    engine.runAndWait()
