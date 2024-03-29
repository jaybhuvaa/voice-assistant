import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from speech_to_text import *
from selenium.webdriver.support.ui import Select
import whisper
import sounddevice as sd
import wave
import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="jay81",
    database="voice_assistant"
)


def save_data(fname,lname,message,gender,intrests,country):
    cursor = conn.cursor()
    # SQL query to insert data
    sql = "INSERT INTO form_data (f_name,l_name,message,gender,intrests,country) VALUES (%s,%s,%s,%s,%s,%s)"

    values = (fname, lname, message, gender, intrests, country)

    # Execute the query
    cursor.execute(sql,values)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()


def take_data(value):
    try:
     wav_filename = "output.wav"
     speak('tell me your' + value)
     record_audio(wav_filename, duration=5)
     command=speech_to_text(wav_filename)
     go=command.lower()
     print("You said:", go)
     return go
    except sr.UnknownValueError:
        speak("Sorry, could not understand the audio.")
        return take_data(value)
    except sr.RequestError as e:
        speak("Could not request results from Whisper service; {0}".format(e))
        return take_data(value)

chrome_driver = r'C:\Users\darsh\Downloads\chromedriver_win32 (1)'

def speech_to_text(file_name):
    model = whisper.load_model("base.en")
    result = model.transcribe(file_name, fp16=False)
    # mel = whisper.log_mel_spectrogram(file_name).to(model.device)
    # _, probs = model.detect_language(mel)
    # print(f"Detected language: {max(probs, key=probs.get)}")
    return(result["text"])

def record_audio(filename, duration=3, samplerate=44100):
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
     speak("What do you want me to do?")
     command = take_data("command")   
     if "fill form" or "feel form" in command:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=chrome_options)
        url = r'C:\Users\darsh\Desktop\Voice Assistant\backend\from.html' 
        #driver = webdriver.Chrome()  # You can use other browser drivers like Firefox or Edge
        driver.implicitly_wait(10)  # Implicit wait to wait for elements to be located
        flag=0;
        gender_options = {
            " male": "male",
            " female": "female",
            " other": "other",
            " prefer_not_say": "prefer_not_say",
            " male.": "male",
            " female.": "female",
            " other.": "other",
            " prefer_not_say.": "prefer_not_say",
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

             cmd=take_data("command")
             if "submit" in cmd:
              try:
                # Assuming you have form data in variables fname, lname, message, intrests, and country
                fname = driver.find_element(By.ID, "firstName").get_attribute("value")
                lname = driver.find_element(By.ID, "lastName").get_attribute("value")
                message = driver.find_element(By.ID, "message").get_attribute("value")
                print(fname, lname, message)
        
                gender_radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='gender']")


                selected_radio = next((radio for radio in gender_radio_buttons if radio.is_selected()), None)

                if selected_radio:
  
                     gender_value = selected_radio.get_attribute("value")

                     print(gender_value)
                else:
                     print("No radio button selected")

                
               # Assuming 'intrests' is a checkbox field
                intrests_checkboxes = driver.find_elements(By.NAME, "hobbies")
                intrests_values = [checkbox.get_attribute("value") for checkbox in intrests_checkboxes if checkbox.is_selected()]
                print(intrests_values)

                # Assuming 'country' is a select dropdown field
                country_select = driver.find_element(By.ID, "country")
                country_value = Select(country_select).first_selected_option.text
                print(country_value)

                # Call the save_data method to save the form data to the database
                save_data(fname, lname, message,gender_value, ",".join(intrests_values), country_value)
                driver.execute_script("submitForm();")
                speak("Form Submitted")
                driver.quit()

              except Exception as e:
                    print(e)
                    speak("An error occurred. Please try again.")
                    break

             
        except Exception as e:
            print(e)
            speak("An error occurred. Please try again.")
            break   
     elif "exit" in cmd:
                print("Exiting program.")
                break   


# fn='darshan'
# ln='patel'
# msg='hello how are you'
# gen='male'
# intr='reading'
# cont='usa'

# save_data(fn,ln,msg,gen,intr,cont)

     
