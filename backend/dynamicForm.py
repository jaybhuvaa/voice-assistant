import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from speech_to_text import *
from selenium.webdriver.support.ui import Select

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
    
def get_radio_options(element):
   options = element.find_elements(By.XPATH, './label')
   return [option.text.lower() for option in options] 

def get_checkbox_options(element):
    options = element.find_elements(By.XPATH, './label')
    return [option.text.lower() for option in options] 


def handle_radio_option(element, options):
    

    command = take_data(f"select {element.get_attribute('name')}")
    print(command, options )
    for option in options:
        print(command, option)
        if option.getAttribute('value') in command:
            print(f"Selecting radio option: {option}")
            element.click()
            break

def handle_checkbox_option(element, options):
    field_id = element.get_attribute("value")

    command = take_data(f"{field_id} checkbox option")
    print(command, options ,field_id)
    for option in options:
        print(command, option)
        if option.lower() in command:
            print(f"Selecting checkbox option: {option}")
            element.click()
            break

def get_dropdown_options(element):
    # Assuming the dropdown input element is passed as a parameter

    # Click on the input field to open the dropdown (if necessary)
    element.click()

    # Wait for the options to be visible (adjust the timeout as needed)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dropdown-options')))

    # Get all available options
    options = element.find_elements(By.CSS_SELECTOR, '.dropdown-options')  # Adjust the selector based on your HTML structure

    # Extract option text
    option_texts = [option.text for option in options]

    return option_texts

def handle_text_dropdown_option(element):
    # Assuming the dropdown input element is passed as a parameter

    # Get all available options
    options = get_dropdown_options(element)

    # Take voice input to select an option
    command = take_data(f"select {element.get_attribute('id')} option")

    # Iterate through options and type the one matching the voice command
    for option in options:
        if option.lower() in command:
            print(f"Selecting dropdown option: {option}")
            element.send_keys(option)
            break

def fill_form(url):
    browser = webdriver.Chrome()
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//input | textarea | select')))
    form_elements = browser.find_elements(By.XPATH, '//input | textarea | select')
    num_fields = len(form_elements)
    print(f"There are {num_fields} fields in the form.")
           
    field_names = [element.get_attribute("id") for element in form_elements]
    print(field_names)
    for element in form_elements:
        field_type = element.get_attribute("type")
        field_id = element.get_attribute("id")
        print(field_type)

        if field_type == "text" or field_type == "textarea":
            continue
            # Handle text input fields
            #speak("Tell me your" + field_id)
            field_value = take_data(field_id)
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, element.get_attribute("id"))))
            element.send_keys(field_value)
        elif field_type == "radio":
            continue
            # Handle radio options
            command = take_data("select " + field_id)
            if 'select' in command:
               label_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='" + element.get_attribute('id') + "']")))
               label_element.click()
        elif field_type == "checkbox":
            continue
            command = take_data("select " + field_id)
            if 'select' in command:
                element.click()
        elif field_type == "text" and "react-select" in field_id:
            # Handle text-based dropdown
            handle_text_dropdown_option(element)

        # elif field_type == "file":
        #     speak("Tell me your" + field_id)
        #     # Handle file input
        #     # Replace 'path/to/file.txt' with the actual file path you want to upload
        #     element.send_keys('path/to/file.txt')
         # Submit the form (adjust the XPath based on the structure of the form)
     # Switch to the iframe
    iframe = WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))

    # Find and click the submit button inside the iframe
    submit_button = WebDriverWait(iframe, 10).until(EC.element_to_be_clickable((By.ID, 'submit')))
    submit_button.click()

fill_form('https://demoqa.com/automation-practice-form')
