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
def listen():
	with sr.Microphone() as source:
		audio = r.listen(source)
		return r.recognize_google(audio)



while True:
	get = listen()
	if(get == 'exit'):
		quit()
	put = speak(get)
