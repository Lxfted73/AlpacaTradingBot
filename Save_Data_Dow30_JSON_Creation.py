import re
import alpaca_trade_api as tradeapi
import json
from datetime import datetime
from pandas import Timestamp

# Replace these with your own Alpaca API keys
API_KEY = 'PKD25Q6FS0P6DJGUNZHY'
SECRET_KEY = 'qshvbGNMKaIfP8DfPw8Z78whpWetIGNgoZSyOgzH'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use paper trading base URL for testing

#Initialize the Alpaca API Client
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')


# #Collect Historical Market Data
# symbol = 'AAPL'
timeframe = '1D'
start_date = '2022-01-01'
end_date = '2022-01-31'

# List to store extracted symbols
symbols = []

# Open the text file
with open('Dow30_Tickers.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Use regular expression to extract symbol
        match = re.search(r'^([A-Z]+)\s+\(', line)
        if match:
            symbols.append(match.group(1))

historical_data = api.get_bars(symbols, timeframe = timeframe, start = start_date, end = end_date)


formatted_data = []
for bar in historical_data:
        formatted_data.append({
            'Symbol': bar.S,
            'Timestamp': [bar.t.strftime('%Y-%m-%d %H:%M:%S')],
            'Open': bar.o,
            'High': bar.h,
            'Low': bar.l,
            'Close': bar.c,
            'Volume': bar.v
        })
# print(f"formatted_data {formatted_data[1]}")
json_string = json.dumps(formatted_data)
# print(f"json_string {json_string}")
data = json.loads(json_string)
# print(f"json_loads: {data}")
file_path = 'Dow30_json.json'

# Write JSON string to a file
with open(file_path, 'w') as json_file:
    json_file.write(json_string)

