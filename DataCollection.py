import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt


# Replace these with your own Alpaca API keys
API_KEY = 'PKD25Q6FS0P6DJGUNZHY'
SECRET_KEY = 'qshvbGNMKaIfP8DfPw8Z78whpWetIGNgoZSyOgzH'
BASE_URL = 'https://paper-api.alpaca.markets'  # Use paper trading base URL for testing

#Initialize the Alpaca API Client
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')



#Collect Historical Market Data
symbol = 'AAPL'
timeframe = 'day'
start_date = '2022-01-01'
end_date = '2022-01-31'

historical_data = api.get_bars(symbol, timeframe = '1H', start = start_date, end = end_date)
print(historical_data)
if isinstance(historical_data, list):
    print("Shape of historical_data:", len(historical_data))
elif isinstance(historical_data, dict):
    print("Keys in historical_data:", historical_data.keys())

#Extract OHLC Data from the historical_data variable
dates = [bar.t for bar in historical_data]
opens = [bar.o for bar in historical_data]
highs = [bar.h for bar in historical_data]
lows = [bar.l for bar in historical_data]
closes = [bar.c for bar in historical_data]
volumes = [bar.v for bar in historical_data]


#Plot OHLC data
plt.figure(figsize=(10, 6))
plt.plot(dates, closes, label = 'Close')
plt.plot(dates, highs, label = 'High')
plt.plot(dates, lows, label = 'Low')
#plt.plot(dates, volumes, label = 'Volume')
plt.title("Historical OHLC Data for {}".format(symbol))
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()


