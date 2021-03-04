import re
intent_keywords = {
    'self':['your','you','yourself'],
    'greet': ['hi','morning','hello','welcome','Hey','Nice to meet you'],
    'time': ['time', 'clock'],
    'date':['date','day','calendar','today'],
    "search":['search',"when","what","why","how","who","where"],
    'relax':["relax"],
    'location':['find','track'],
    'close': ['close'],
    'exit':['close','shut up','stop','exit']
}

patterns = {intent: re.compile('|'.join(keys)) for intent, keys in intent_keywords.items()}

def get_intent(message):
    intents=[]
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        if pattern.search(message):
            intents.append(intent)
    if(len(intents)!=0):
        return intents
    else: 
        return(['default']) 
def ques_check(message):
    que = False
    for i in ["when","what","why","how","who","where"]:
        if i in message:
            que = True
            return que