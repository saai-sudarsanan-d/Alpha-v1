import datetime
from datetime import datetime
import webbrowser
import random
from intent_keys import get_intent, ques_check
from talk import speak

search_ques = ["when","what","why","how"]
loc_ques = ["where"]
greet_list = ['Hi','Hello','Welcome','Hey there']
date_list = ['Today is ','Today\'s date is ','I woke up to find the calendar showing ','My calendar shows ','I think today is ','Guess it is ']
time_list = ['Tic-tok ','Clock shows ','My clock shows ','According to the magical mysteries of the blackhole...it is ','It is precisely ','You are now wasting ','I guess it is ']
end_list = ['See ya','Bye','Sad to see you go','Good Bye','Have a nice day...bye','See ya later, alligator!','Don\'t get run over!','Long live and prosper','Fare Thee Well']
search_list = ['Here you go','3...2...1...','Here\'s your result!','I got you...here...','Just a minute','Gimmie a second!','In a minute','Almost done!']

#Selects a random value from the list of responses
def rand_select(list_of_values):
    size = len(list_of_values)
    selector = random.randint(0,size-1)
    return list_of_values[selector]

#Just a few things about the Bot itself
def extras(message):
    r = 1
    name_bool = False
    if 'name' in message:
            if 'change' in message:
                speak('Sorry, you cannot change my name. Saai won\'t let me, I think Alpha is a great name')
            else:
                if(name_bool == False):
                    speak('My name is Alpha. I am a chatbot')
                    name_bool = True
    if 'where' in message:
        speak("I don't have any particular place of stay")

    if 'about' in message:
        if(name_bool == False):
            speak('''My name is Alpha. I am the 2nd version of the Alpha that is being created by my creator 
                Saai Sudarsanan. I like eating power that comes from solar energy. I hate it when people waste electricity, since that is my food.
                I don't have any particular place of stay. Well, that is it about me.''')
        else:
            speak('''I am the 2nd version of the Alpha that is being created by my creator 
                Saai Sudarsanan. I like eating power that comes from solar energy. I hate it when people waste electricity, since that is my food.
                I don't have any particular place of stay. Well, that is it about me.''')
    if 'favourite' in message:
        if 'food' in message:
            speak('I like eating power that comes from solar energy. I hate it when people waste electricity, since that is my food.')
        if 'place' in message:
            speak('I like the green scapes of thanjavur and the delta regions in Tamilnadu')
        if 'actor' in message:
            speak('Saai and I have similar tastes, we both like Rowan Atkinson, a-k-a Mr.Bean...Here is a scene I personally like...')
            webbrowser.open('https://www.youtube.com/watch?v=2v3mLxd2FfA')
            r = 2
    if 'creator' in message:
        speak('I was made by Saai Sudarsanan D, just a few days before his final exams,because he was too bored to do math and wanted to chill.')
        if 'kaggle' in message:
            speak('Here is Saai\'s kaggle profile!')
            webbrowser.open('https://www.kaggle.com/saaisudarsanand')
            r = 2
        if 'github' in message:
            speak('Here is Saai\'s Github Repo!')
            webbrowser.open('https://github.com/saai-sudarsanan-d')
            r = 2
    return r

def respond(message):
    vd = get_intent(message)
    ans_que = False
    r = 1
    sleep_bool = False

    if "relax" in vd:
        sleep_bool = True
        r = 2

    if 'default' in vd:
        r = 0

    if 'self' in vd:
        ans = extras(message)
        ans_que = False
        r = ans

    if 'greet' in vd:
        speak(rand_select(greet_list))
        ans_que = False
        r = 1

    if "date" in vd:
        speak(rand_select(date_list) + datetime.now().strftime("%d-%m-%Y"))
        ans_que = False
        r = 1

    if "time" in vd:
        speak(rand_select(time_list) + datetime.now().strftime("%H:%M:%S"))
        ans_que = False
        r = 1
        
    if ("exit" in vd):
        speak(rand_select(end_list))
        ans_que = False
        r = -1

    if "search" in vd and len(vd)==1:
        ans_que = True

    if "search" in vd:
        if ans_que:
            if "search" in message:
                search_element = message.partition("search ")[2].split(" ")[0]
                url = "https://www.google.com/search?q=" + search_element
                speak(rand_select(search_list))
                webbrowser.open(url)
                sleep_bool = True
            elif(ques_check):
                url = "https://www.google.com/search?q=" + message
                speak(rand_select(search_list))
                webbrowser.open(url)
                sleep_bool = True

    if(sleep_bool):
        return 2
    else:
        return r