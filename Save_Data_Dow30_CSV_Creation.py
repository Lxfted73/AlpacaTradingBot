import csv
import re
import alpaca_trade_api as tradeapi
import json
from datetime import datetime
from pandas import Timestamp


# Load JSON data from a file
try:
    file_path = 'Dow30_json.json'
    with open(file_path, 'r') as file:
        json_data = json.load(file)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except json.decoder.JSONDecodeError as e:
    print(f"Error decoding JSON data in file '{file_path}': {e}")
else:
    print("JSON data loaded successfully.")

csv_file = 'historical_data.csv'


# Save historical data to a CSV file
def save_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)


# Example usage:
save_to_csv(json_data, 'Dow30_historical_data.csv')