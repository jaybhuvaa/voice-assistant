import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from speech_to_text import *

def take_data(value):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak('tell me your' + value)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, could not understand the audio.")
        return take_data(value)
    except sr.RequestError as e:
        speak("Could not request results from Google Speech Recognition service; {0}".format(e))
        return take_data(value)

chrome_driver = r'C:\Users\darsh\Downloads\chromedriver_win32 (1)'
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""
    
while True:
     command = recognize_speech()   
     if "fill form" in command:
        url = r'C:\Users\darsh\Desktop\Voice Assistant\backend\from.html' 
        form_data = {
            'firstName' : '',
            'lastName' : '',
            'message' : ''
        }   
        driver = webdriver.Chrome()  # You can use other browser drivers like Firefox or Edge
        driver.implicitly_wait(10)  # Implicit wait to wait for elements to be located
        try:
             driver.get(url)
             time.sleep(2)  # Wait for page to load
             for field_name, field_value in form_data.items():
              input_field = driver.find_element("name",field_name)
              field_value=take_data(field_name)
              input_field.send_keys(field_value)
        except Exception as e:
          print("An error occurred:", e)
     elif "exit" in command:
             print("Exiting program.")
             break    
     elif "submit" in command:
      try:
        driver.execute_script("submitForm();")
        speak(" Form Submitted")
      except Exception as e:
        speak("An error occurred")
     
