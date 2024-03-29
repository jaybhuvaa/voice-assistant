import pandas as pd
def write_to_excel():


# Assuming you have a CSV file with your data
    csv_file_path = 'exam.csv'
    excel_file_path = 'data.xlsx'

# Read existing Excel file
    try:
        existing_data = pd.read_excel(excel_file_path)
    except FileNotFoundError:
    # If the file doesn't exist, create a new DataFrame
        existing_data = pd.DataFrame()

# Read new data from CSV file
    new_data = pd.read_csv(csv_file_path)

# Append new data to existing data
    merged_data = existing_data._append(new_data, ignore_index=True)

# Write merged data to Excel file
    with pd.ExcelWriter(excel_file_path, mode='a', engine='openpyxl',if_sheet_exists="overlay") as writer:
        merged_data.to_excel(writer, index=False, sheet_name='data')

#write_to_excel()