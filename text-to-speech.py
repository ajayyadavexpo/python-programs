import pyttsx3
engine = pyttsx3.init();
voices = engine.getProperty('voices')
#by default 200 words per minute
newVoiceRate = 130
engine.setProperty('rate', newVoiceRate)
#female voice 
engine.setProperty('voice', voices[1].id) 
 #male voice 
#engine.setProperty('voice', voices[0].id)

filename = "paragraph.txt"
f = open(filename, "r")
engine.say(f.read())

engine.runAndWait()

