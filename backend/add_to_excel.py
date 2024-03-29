from speech_to_text import *
from data_to_csv import *
from csv_to_excel import *
from config import *

def add_data_to_excel():
    speak("Roll Number please")
    roll_number=takeData()
    print(roll_number)
    speak(f'you have entered {roll_number}')
    speak("are you sure?")
    agree=takeData()
    print(agree)

    if agree=="sure":

        speak("marks please")
        marks=int(takeData())
        print(marks)
        speak(f'you have entered {marks}')

        speak("please confirm it,is it okay?")
        confirm=takeData();
        if confirm=="sure":

            if isValidFormat(roll_number) & isInRange(marks):
                write_in_csv(roll_number,marks)
                write_to_excel()
            else:
                speak("You have entred worng format for roll number or marks is out of range")
                print("Error in format")
                add_data_to_excel()
        else:
            add_data_to_excel()
    else:
       add_data_to_excel()
    
    speak("do you want to continue?")
    res=takeData()
    if res=="sure":
        add_data_to_excel()
    else:
        speak("Thank you for submitting data")

# add_data_to_excel()

# while(True):    
#     add_data_to_excel()


    

