import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from speech_to_text import *

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
def take_data():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("tell me your data")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, could not understand the audio.")
        return take_data()
    except sr.RequestError as e:
        speak("Could not request results from Google Speech Recognition service; {0}".format(e))
        return take_data()

def fill_out_form(url, form_data):
    driver = webdriver.Chrome()  # You can use other browser drivers like Firefox or Edge
    driver.implicitly_wait(10)  # Implicit wait to wait for elements to be located
    
    try:
        driver.get(url)
        time.sleep(2)  # Wait for page to load
        input_field = driver.find_element("name","firstName")
        input_field.send_keys(form_data['firstName'])
        for field_name, field_value in form_data.items():
            input_field = driver.find_element("name",field_name)
            input_field.send_keys(field_value)
            
        
        # submit_button = driver.find_element("xpath","//button[@type='submit']")  # Assuming submit button is a <button> element
        # submit_button.click()
        
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")) )
        submit_button.click()

        # time.sleep(2)  # Wait for the form submission to complete

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    url = r'C:\Users\darsh\Desktop\Voice Assistant\backend\from.html'  # Replace with actual URL of the form
    form_data = {
        'fistName' : '',
        'lastName' : '',
        'email'  : '',
        'message' : ''
    
    }

    while True:
        command = recognize_speech()
        if "exit" in command:
            print("Exiting program.")
            break
        elif "fill form" in command:
            speak("Listening for form data...")
            form_data['firstName'] = take_data()
            form_data['lastName'] = take_data()
            form_data['email'] = take_data()
            form_data['message'] = take_data()
            
            print("Filling out form...")
            fill_out_form(url, form_data)
            print("Form filled successfully.")
        else:
            print("Command not recognized. Please try again.")
