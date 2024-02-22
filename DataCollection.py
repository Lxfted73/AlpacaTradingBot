import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt


# Replace these with your own Alpaca API keys
API_KEY = 'PKD25Q6FS0P6DJGUNZHY'
SECRET_KEY = 'qshvbGNMKaIfP8DfPw8Z78whpWetIGNgoZSyOgzH'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use paper trading base URL for testing

#Initialize the Alpaca API Client
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')





# #Collect Historical Market Data
# symbol = 'AAPL'
timeframe = 'day'
start_date = '2022-01-01'
end_date = '2022-01-31'
import re

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


# Print the list of symbols
print(symbols)

historical_data = api.get_bars(symbols, timeframe = '1D', start = start_date, end = end_date)
print(f"historicaldata[1]: {historical_data[1]}")
print(f"historicaldata[2]: {historical_data[2]}")
if isinstance(historical_data, list):
    print("Shape of historical_data:", len(historical_data))
elif isinstance(historical_data, dict):
    print("Keys in historical_data:", historical_data.keys())

#Extract OHLC Data from the historical_data variable
symbol = [bar.S for bar in historical_data]
dates = [bar.t for bar in historical_data]
opens = [bar.o for bar in historical_data]
highs = [bar.h for bar in historical_data]
lows = [bar.l for bar in historical_data]
closes = [bar.c for bar in historical_data]
volumes = [bar.v for bar in historical_data]


#Print the first 5 symbols
symbols = list(historical_data[:5])
for ticker in symbols:
    symbol = [bar.S for bar in symbols]
    dates = [bar.t for bar in symbols]
    opens = [bar.o for bar in symbols]
    highs = [bar.h for bar in symbols]
    lows = [bar.l for bar in symbols]
    closes = [bar.c for bar in symbols]
    volumes = [bar.v for bar in symbols]
print(symbols)


# for symbol in symbols:
#     #Plot OHLC data
#     plt.figure(figsize=(10, 6))
#     plt.plot(dates, closes, label = symbol.S)
#     #plt.plot(dates, highs, label = 'High')
#     #plt.plot(dates, lows, label = 'Low')
#     #plt.plot(dates, volumes, label = 'Volume')
#     plt.title("Historical OHLC Data for 30 Dow Tickers")
#     plt.xlabel("Date")
#     plt.ylabel("Price")
#     plt.legend()
#     plt.grid(True)
# plt.show()

# plt.figure(figsize=(10, 6))
# for bars in historical_data:
#     plt.plot(dates, closes, label=symbols)
# plt.title("Historical Data 30 Dow Tickers")
# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.legend()
# plt.grid(True)
# plt.show()


