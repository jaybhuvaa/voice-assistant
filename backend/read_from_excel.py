import pandas as pd
from speech_to_text import *
file_path=r'C:\Users\darsh\Desktop\Voice Assistant\backend\data.xlsx'

yo=pd.read_excel(file_path)
speak(yo)
print(yo)