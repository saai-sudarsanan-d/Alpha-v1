import speech_recognition as sr
import time
from respond import respond
from talk import speak
import os

#The Recognizers for Speech Data
r = sr.Recognizer() #-> General
wake = sr.Recognizer() #-> Wake word

#Clears Screen after each output
def clear(): 
    os.system("cls||clear")
class wakey:
    def activate():
        with sr.Microphone() as source:
            print('I am going to sleep...say "Hello Alpha" in order to get me working')
            print('Sleeping...zzzzz....zzzzz')
            while True:
                # audio = r.listen(source)
                # wake_word = ""
                # try:
                #     wake_word = r.recognize_google(audio)
                # except sr.UnknownValueError:
                #     pass
                # except sr.RequestError:
                #     speak("Sorry, my Speech service is down!")
                wake_word = str(input())
                if ("alpha" in wake_word.lower()):
                    break
        return wake_word

#Function to Record Audio
# def rec_audio(ask=False):
#     #Open the Microphone
#     with sr.Microphone() as source:
#         if ask:
#             speak(ask)
#         print("Listening...")
#         audio = r.listen(source)
#         voice_data = ""
#         #Error Handling
#         try:
#             voice_data = r.recognize_google(audio)
#         except sr.UnknownValueError:
#             speak("Sorry, I did not get that!")
#             voice_data = '-1_sr_error'

#         except sr.RequestError:
#             speak("Sorry, my Speech service is down!")
#             voice_data = '-1_sr_error'

#     return voice_data

def rec_audio():
    print("Listening...")
    voice_data = str(input())
    return voice_data

#Allows Alpha to stay on, 
time.sleep(3)
speak("How can I help you")
check = 1
while(check in [0,1,2]):
    if(check == 1):
        voice_data = rec_audio()
        if(voice_data == "-1_sr_error"):
            continue
    elif(check == 2):
        wakey.activate()
        check = 1
        continue
    else:
        check = 1
        continue
    check = respond(voice_data.lower())
    clear()