import csv
def write_in_csv(rn,mk):
    # Data to be appended
    data_to_append = [rn,mk]

# CSV file path
    csv_file_path = "exam.csv"

# Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='') as file:
    # Create a CSV writer object
        csv_writer = csv.writer(file)

    # Append the data to the CSV file
        csv_writer.writerow(data_to_append)

# write_in_csv(2,23)
# write_in_csv(3,25)
# write_in_csv(4,455)




