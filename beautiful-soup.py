import requests 
from bs4 import BeautifulSoup 
import re
import pyttsx3 as pytx
import speech_recognition as sr

r = sr.Recognizer()
engine = pytx.init();
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[0].id) 

def speak(txt):
    engine.say(txt)
    engine.runAndWait()
    print('.')
    
def listen():
    print('........')
    with sr.Microphone() as source:
        audio = r.listen(source)
        return r.recognize_google(audio)


  

def search_text(text):
    url = "https://en.wikipedia.org/wiki/"
    r = requests.get(url+text.replace(" ","_"));
    soup = BeautifulSoup(r.content, 'html5lib') 
    class_name = soup.find('div', attrs = {'id':'mw-content-text'}) 
    class_name = class_name.find('div', attrs = {'class':'mw-parser-output'}).findAll('p')
    content = ''
    for row in class_name:
        content += row.text
    content = re.sub(r'\d[^\w]+', ' ',content)
    content = content.split('.')
    sort = content[0]+content[1]
    

    print(sort)
    speak(sort)

while True:
    speak('Hello , How may i help you')
    get = listen()
    search_key = ['please search','search please','search','search on web']
    exit_key = ['bye bye','please exit','exit','close']
    if(get in search_key):
        speak('What you want to search')
        search = listen()
        search_text(search)

    if(get in exit_key):
        exit()






