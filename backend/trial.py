from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
from selenium.webdriver.chrome.service import Service

# Replace with your browser's WebDriver path
driver_path = r'C:\Users\darsh\Downloads\chromedriver_win32 (1)'






# Replace with the URL containing the radio buttons
webpage_url = r'C:\Users\darsh\Desktop\Voice Assistant\backend\from.html'

gender_options = {
    "male": "male",
    "female": "female",
    "other": "other",
    "prefer_not_say": "prefer_not_say"
}

# Initialize the browser and open the webpage
driver = webdriver.Chrome()
driver.get(webpage_url)

# Function to select radio button based on voice command
def select_gender_by_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your choice (male, female, other, or prefer not to say):")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        if command in gender_options:
            radio_button = driver.find_element(By.ID, gender_options[command])
            radio_button.click()
            print(f"Selected: {command}")
        else:
            print("Invalid choice. Please try again.")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Request failed: {e}")

# Call the function to listen for voice command and select
select_gender_by_voice()

# Close the browser
driver.quit()