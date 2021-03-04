import pyttsx3 as pytts

#Defining the Text-To-Speech Engine
tts = pytts.init()
tts.setProperty('rate', 175)    #Set Word Rate(word/minute)
tts.setProperty('volume', 1)    #set Volume(0 -> 1)
voices = tts.getProperty('voices')  
tts.setProperty('voice', voices[0].id)  #Set Voice ID(Male/Female)

#Function to Speak
def speak(audio_string):
    tts.say(audio_string)
    print(audio_string)
    tts.runAndWait()