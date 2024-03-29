# # importing all the 
# # functions defined in test.py
# from testing.test import display


# # calling functions
# display()
# var="hello"
# print('hyyy'+ var)
# form_data = {
#             'firstName' : 'jay',
#             'lastName' : 'bhuva',
#             'email'  : 'jay@gmaiol.com',
#             'message' : 'hello'
#         }   
# for field_name, field_value in form_data.items():
#     print(field_name)
#     print(field_value)

import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = r'C:\Users\darsh\Desktop\Voice Assistant\backend\from.html' 
driver = webdriver.Chrome()  # You can use other browser drivers like Firefox or Edge
driver.implicitly_wait(10)  # Implicit wait to wait for elements to be located
try:
     driver.get(url)
     time.sleep(2)  # Wait for page to load
     submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
     submit_button.click()
     print("done")
except Exception as e:
          print("An error occurred:", e)