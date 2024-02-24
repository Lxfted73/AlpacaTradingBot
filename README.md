## Title: Financial Indicators Analysis for Dow 30 Tickers

### Description:

This Python script conducts detailed analysis of financial indicators for Dow 30 tickers using historical market data and technical analysis tools. It processes historical market data for the Dow 30 tickers, computes various technical indicators such as moving averages, trend indicators, momentum indicators, volatility indicators, and volume indicators, and visualizes these indicators using both Matplotlib and Plotly libraries. Additionally, the script interfaces with the Alpaca API to collect historical market data.

### Key Features:

- **Data Collection:** Loads historical market data for Dow 30 tickers from a CSV file and collects additional data from the Alpaca API.
- **Preprocessing:** Processes and preprocesses the data, including converting timestamps to datetime format.
- **Technical Indicators:** Computes a variety of technical indicators, including moving averages, trend indicators (e.g., ADX, MACD), momentum indicators (e.g., RSI, Stochastic), volatility indicators (e.g., Bollinger Bands), and volume indicators (e.g., OBV, CMF).
- **Visualization:** Generates insightful charts and graphs to visualize the computed indicators using both Matplotlib and Plotly libraries.
- **API Integration:** Interfaces with the Alpaca API to collect historical market data for further analysis.

### Skills Highlighted:

- **Python Scripting:** Proficient in writing Python scripts for financial data analysis, including data preprocessing, computation of technical indicators, and visualization of results.
- **Financial Analysis:** Skilled in analyzing financial market data and computing a wide range of technical indicators to identify trends and patterns.
- **Data Visualization:** Experienced in creating visually appealing charts and graphs using Matplotlib and Plotly libraries to present analysis results effectively.
- **API Integration:** Familiar with integrating external APIs, such as the Alpaca API, to collect real-time or historical market data for analysis.
- **Technical Proficiency:** Well-versed in utilizing libraries and tools like Pandas, TA-Lib, Plotly, and Matplotlib for conducting comprehensive financial analysis.
- **Problem Solving:** Strong problem-solving skills in addressing challenges related to data processing, indicator computation, and visualization tasks.
- **Collaboration:** Open to collaboration and contributions, with a willingness to work in a team environment and share knowledge with peers.

### Example Usage:

```python
# Load historical market data from CSV file
df = pd.read_csv('Data_Collection/Dow30_historical_data_1H.csv')

# Preprocess the data
df['Timestamp'] = pd.to_datetime(df['Timestamp'].str.strip("[]"))

# Compute technical indicators
for group_name, group_df in grouped_data:
    # Compute various technical indicators
    group_df['SMA_2'] = group_df['Close'].transform(lambda x: x.rolling(window=2).mean())
    group_df['ADX'] = ta.trend.adx(group_df['High'], group_df['Low'], group_df['Close'])
    # Add more indicators as needed...

# Visualize indicators using Matplotlib or Plotly
# Example: Plot Moving Average Indicators using Plotly
fig1 = go.Figure()
close = go.Scatter(x=group_df.index, y=group_df['Close'], mode='lines', name='Close')
trace_ma_2 = go.Scatter(x=group_df.index, y=group_df['SMA_2'], mode='lines', name='MA (10)')
fig1.add_trace(close)
fig1.add_trace(trace_ma_2)
fig1.update_layout(title='Moving Average Indicators', xaxis_title='Timestamp', yaxis_title='Value')
fig1.show()
