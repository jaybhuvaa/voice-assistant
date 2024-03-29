import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By

def find_and_fill_form():
    # Set up the voice assistant
    recognizer = sr.Recognizer()

    # Set up the web browser (make sure to have the appropriate webdriver installed)
    browser = webdriver.Chrome()

    # Voice command to start the process
    with sr.Microphone() as source:
        print("Say 'find form' to initiate the process.")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")

            if "find form" in command.lower():
                # Navigate to the webpage
                form_url = r"C:\Users\darsh\Desktop\Voice Assistant\backend\from.html"
                browser.get(form_url)

                # Find and count the form elements
                form_elements = browser.find_elements(By.XPATH, '//input')
                num_fields = len(form_elements)
                print(f"There are {num_fields} fields in the form.")

                # Print the names of the fields
                field_names = [element.get_attribute("name") for element in form_elements]
                print("Field names:")
                for name in field_names:
                    print(f"- {name}")

                # Ask user to fill the form
                print("Would you like to fill out the form? Say 'yes' or 'no'.")
                audio = recognizer.listen(source)
                response = recognizer.recognize_google(audio)

                if "sure" in response.lower():
                    # Provide instructions for filling out the form
                    print("Please provide values for the following fields:")

                    for name in field_names:
                        print(f"What should be the value for the field {name}?")
                        audio = recognizer.listen(source)
                        field_value = recognizer.recognize_google(audio)
                        # Use Selenium to fill the form fields
                        browser.find_element(By.NAME, name).send_keys(field_value)

                    print("Form filled successfully!")

                else:
                    print("Alright, not filling out the form.")

            else:
                print("Sorry, I didn't understand the command.")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    # Close the browser
    browser.quit()

if __name__ == "__main__":
    find_and_fill_form()
