import re
import alpaca_trade_api as trade_api
import json



API_KEY = ''
SECRET_KEY = ''
BASE_URL = 'https://paper-api.alpaca.markets'
timeframe = ''
start_date =''
end_date = ''
json_file_path = ''
ticker_file_path = ''

class createJSON():
    def __init__(self, API_KEY, SECRET_KEY, BASE_URL, json_file_path, ticker_file_path):
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.BASE_URL = str(BASE_URL)
        self.timeframe = ''
        self.start_date = ''
        self.end_date = ''
        self.json_file_path = json_file_path
        self.ticker_file_path = ticker_file_path

    def set_timeframe(self, timeframe):
        self.timeframe = timeframe

    def set_start_date_and_end_date(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def load_tickers_file_path(self, ticker_file_path):
        self.ticker_file_path = ticker_file_path

    def set_keys_and_base_url(self, API_KEY, SECRET_KEY):
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.BASE_URL = BASE_URL  # Use paper trading base URL for testing
    def createJSON(self):

        """
        Consolidate into a function that can be used to create both 1D and 1H Files."
        """

        api = trade_api.REST(self.API_KEY, self.SECRET_KEY, self.BASE_URL, api_version='v2')

        # List to store extracted symbols
        symbols = []

        # Open the text file
        with open(self.ticker_file_path, 'r') as file:
            # Read each line in the file
            for line in file:
                # Use regular expression to extract symbol
                match = re.search(r'^([A-Z]+)\s+\(', line)
                if match:
                    symbols.append(match.group(1))

        historical_data = api.get_bars(symbol = symbols, timeframe = self.timeframe, start = self.start_date, end = self.end_date)

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


        # Write JSON string to a file
        with open(self.json_file_path, 'w') as json_file:
            json_file.write(json_string)

