import csv
import json

# Function to convert CSV to JSON
def csv_to_json(csv_file_path, json_file_path):
    # Open the CSV file
    with open(csv_file_path, mode='r', encoding='ISO-8859-1') as csv_file:
        # Read the CSV file
        csv_reader = csv.DictReader(csv_file)

        # Create an empty list to store the rows
        data = []

        # Loop through each row in the CSV and add it to the list
        for row in csv_reader:
            data.append(row)

    # Write the list to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# Replace with your file paths
csv_file_path = 'training_data.csv'  # Path to your CSV file
json_file_path = 'trainingData.json'  # Path to save the JSON file

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)

print("CSV has been successfully converted to JSON!")
