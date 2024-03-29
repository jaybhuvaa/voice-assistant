from add_to_excel import*
from speech_to_text import *
from data_to_csv import *
from csv_to_excel import *
from config import *


def init2():
    speak("What can i do for you?")

    query=takeData();
    print(query)
    if query=="I want to submit data":
        speak("Okay, so whenever you are ready just say start")

        take=takeData();
        print(take)
        if take=="start":
            add_data_to_excel()
            
def init():
    init=takeData()
    print(init)

    if init=="hey Lucy":
        init2()
    else:
        inp=takeData()
        if inp=="hey Lucy":
            init2()

init()


