# import requests
# from bs4 import BeautifulSoup

# # Replace 'your_spreadsheet_url' with the actual URL of the spreadsheet you want to scrape
# spreadsheet_url = 'https://docs.google.com/spreadsheets/d/11zAV3MAxM-WmS2uddKZBwHXjsIwkTB3Voe4tS7UUmhs/edit#gid=0'

# # Make a GET request to the URL
# response = requests.get(spreadsheet_url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the page using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract data based on the HTML structure of the page
#     # Example: find all table rows and print the text content
#     for row in soup.find_all('tr'):
#         print(row.get_text())
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets API credentials (replace 'your-credentials.json' with your actual credentials file)
credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\darsh\Desktop\Python\keys.json', ['https://spreadsheets.google.com/feeds'])

# Authenticate with the Google Sheets API
gc = gspread.authorize(credentials)

# Replace 'your_spreadsheet_key' with the actual key of your Google Sheet
spreadsheet_key = '11zAV3MAxM-WmS2uddKZBwHXjsIwkTB3Voe4tS7UUmhs'

# Open the Google Sheet by key
worksheet = gc.open_by_key(spreadsheet_key).sheet1  # Use the correct sheet name or index

# Get all values from the worksheet
values = worksheet.get_all_values()

# Display the values
for row in values:
    print(row)

