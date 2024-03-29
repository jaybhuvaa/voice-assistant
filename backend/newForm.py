import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from speech_to_text import *
from selenium.webdriver.support.ui import Select
import whisper
import sounddevice as sd
import wave

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

def speech_to_text(file_name):
    model = whisper.load_model("base")
    result = model.transcribe(file_name)
    return(result["text"])

def record_audio(filename, duration=5, samplerate=44100):
    # Record audio
    audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    # Save audio as WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())


def handle_select_option(element):
    options = get_select_options(element)
    print(options)
    element.click()
    command = take_data(f"select {element.get_attribute('id')} option")
    
    for option in options:
        if option.lower() in command:
            print(f"Selecting dropdown option: {option}")
            Select(element).select_by_value(option)
            break

def get_select_options(element):
    select = Select(element)
    options = [option.text.lower() for option in select.options]
    return options

    
while True:
     command = recognize_speech()   
     if "fill form" in command:
        url = r'C:\Users\darsh\Desktop\Voice Assistant\backend\from.html' 
        driver = webdriver.Chrome()  # You can use other browser drivers like Firefox or Edge
        driver.implicitly_wait(10)  # Implicit wait to wait for elements to be located
        flag=0;
        gender_options = {
            "male": "male",
            "female": "female",
            "other": "other",
            "prefer_not_say": "prefer_not_say"
            }
        hobby_options = {
            "reading": "reading",
            "travelling": "travelling",
            "gaming": "gaming"
        }


        try:
             driver.get(url)
             speak("Form opened")
             WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//input | textarea | select')))
             form_elements = driver.find_elements(By.XPATH, '//input | //textarea | //select')
             num_fields = len(form_elements)
             print(f"There are {num_fields} fields in the form.")
             field_names = [element.get_attribute("id") for element in form_elements]

             for element in form_elements:
                field_type = element.get_attribute("type")
                field_id = element.get_attribute("id")
                print(field_type)

                if field_type == "text" or field_type == "textarea":
                     
                     field_value = take_data(field_id)
                     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, element.get_attribute("id"))))
                     element.send_keys(field_value)
                elif field_type == "radio": 
                 if flag==0:
                   command = take_data(f"{element.get_attribute('name')}")
                   if command in gender_options:
                    radio_button = driver.find_element(By.ID, gender_options[command])
                    radio_button.click()
                    flag=1
                    print(f"Selected: {command}")
                   else:
                    print("Invalid choice. Please try again.")
                 elif flag==1:
                       continue
                 
                elif field_type == "checkbox":
                    
                    command = take_data(f"{element.get_attribute("value")} checkbox option")
                    if 'skip' in command:
                        continue
                    elif 'check' in command:
                        element.click()
                        print(f"Selected: {command}")
                    else:
                        print("Invalid choice. Please try again.")
                elif field_type == "select-one":
                     handle_select_option(element)
        except Exception as e:
             speak("An error occurred")
     elif "exit" in command:
             print("Exiting program.")
             break    
     elif "submit" in command:
      try:
        driver.execute_script("submitForm();")
        speak(" Form Submitted")
      except Exception as e:
        speak("An error occurred")
     
