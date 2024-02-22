import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

from Save_Data_Dow30_CSV_Creation import createCSV
from Save_Data_Dow30_JSON_Creation import createJSON

print_graphs = 'TRUE'
ticker_file_path = 'Dow30_Tickers.txt'
csv_file_path = 'Dow30_historical_data_1D.csv'
json_file_path = 'Dow30_json_1D.json'
API_KEY = 'PK86KPRI77Y6A9LQ0ZL3'
SECRET_KEY = '0Ex9CtepMfIHQaYajTvCeCeg9gbNgyXNQdOJi8T4'
BASE_URL = 'https://paper-api.alpaca.markets'

# json_create = createJSON(API_KEY, SECRET_KEY, BASE_URL, json_file_path, ticker_file_path)
# json_create.set_start_date_and_end_date('2021-01-01', '2023-01-31')
# json_create.set_timeframe("1D")
# json_create.createJSON()
#
# csv_create = createCSV()
# csv_create.setCSVFilePath('Dow30_historical_data_1D.csv')
# csv_create.setJSONFilePath('Dow30_json_1D.json')
# csv_file = csv_create.createCSV()

# Read the csv file
data = pd.read_csv(csv_file_path)
# data['Timestamp'] = pd.to_datetime()
data.set_index(pd.to_datetime(data['Timestamp'].str.strip("[]")), inplace=True)  # Set timestamp column as index
data.sort_index(inplace=True)
# Display basic information about the DataFrame
print("DataFrame Information:")
print(data.info())

# Display summary statistics for numerical columns
print("\nSummary Statistics:")
print(data.describe())

# Display the first few rows of the DataFrame
print("\nFirst few rows of the DataFrame:")
print(data.head(15))


print("\n The first 2 tickers in the DataFrame")
print(data['Symbol'][:2])



grouped = data.groupby('Symbol')
print (f"\nGrouped.head()\n {grouped.head()}")


group_keys = list(grouped.groups.keys())
first_group_key = group_keys[0]
first_group = grouped.get_group(first_group_key)  # Get the DataFrame for the first group
#first_group_head = first_group.head(2)
#print(f"\nFirst_group_head\n {first_group_head}")
print(f"\nfirst_group\n {first_group}")

if print_graphs:
    fig = go.Figure()
    plt.figure(figsize=(10,6))
    # for i in range(3):
    #     current_group_key = group_keys[i]
    #     current_group = grouped.get_group(current_group_key)
    #     plt.plot(current_group['Timestamp'], current_group['Close'])
    #     plt.title(f"{current_group['Symbol'].iloc[1]} - Close Price Over Time")
    #     plt.xlabel("Timestamp")
    #     plt.ylabel("Close Price")
    #     plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    #     plt.grid(True)
    #     plt.tight_layout()
    #     plt.show()

    for i in range(3):
        current_group_key = group_keys[i]
        current_group = grouped.get_group(current_group_key)
        fig.add_trace(go.Scatter(x=current_group['Timestamp'], y=current_group['Close'], mode='lines',
                                 name=current_group_key))

    # Update layout
    fig.update_layout(
        title=str(f"{current_group['Symbol'].iloc[1]} - Close Price Over Time"),
        xaxis_title='Timestamp',
        yaxis_title='Close Price',
        xaxis=dict(tickangle=-45),
        showlegend=True
    )

    # Show the plot
    fig.show()

        #plt.plot(group_df.index, group_df['Close'], label=symbol)


