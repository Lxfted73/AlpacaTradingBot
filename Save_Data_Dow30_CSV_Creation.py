import csv
import json

#global cariables
json_file_path = ""
csv_file_path = ""
class createCSV():
    def __init__(self):
        self.json_file_path = json_file_path
        self.csv_file_path = csv_file_path

    def setJSONFilePath(self, json_file_path = ''):
        self.json_file_path = json_file_path

    def setCSVFilePath(self, csv_file_path = ''):
        self.csv_file_path = csv_file_path
    def createCSV(self, json_file_path=json_file_path, csv_file_path=csv_file_path):
        # Load JSON data from a file
        try:
            file_path = json_file_path
            with open(file_path, 'r') as file:
                json_data = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON data in file '{file_path}': {e}")
        else:
            print("JSON data loaded successfully.")

        # Save historical data to a CSV file
        def save_to_csv(data, csv_file):
            with open(csv_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(json_data)

# Example usage:
# save_to_csv(json_data, csv_file_path)