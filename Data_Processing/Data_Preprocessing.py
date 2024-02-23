import pandas as pd
import ta
import plotly.graph_objs as go
from plotly.subplots import make_subplots

"""Needs Plotly Subplots to be completed """

show_matplotlib = False
show_plotly = False
# 1. Load the CSV File
df = pd.read_csv('Data_Collection/Dow30_historical_data_1H.csv')

# 2. Preprocess the Data (if needed)
# For example, convert the 'Timestamp' column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'].str.strip("[]"))
# df.set_index(pd.to_datetime(df['Timestamp'].str.strip("[]")), inplace=True)  # Set timestamp column as index
# df.sort_index(inplace=True)
# print(df.head())
grouped_data = df.groupby('Symbol')
start_date = df['Timestamp'].min()
end_date = start_date + pd.Timedelta(days=3)
# print(start_date)
# print(end_date)
# print(grouped_data['Symbol'])

pd.set_option('display.max_columns', None)
counter = 0
for group_name, group_df in grouped_data:
    # Moving Averages Indicators
    group_df['SMA_2'] = group_df['Close'].transform(lambda x: x.rolling(window=2).mean())
    group_df['SMA_5'] = group_df['Close'].transform(lambda x: x.rolling(window=5).mean())
    group_df['SMA_10'] = group_df['Close'].transform(lambda x: x.rolling(window=10).mean())
    group_df['EMA_5'] = group_df['Close'].transform(lambda x: ta.trend.ema_indicator(x , window=5))


    # Trend Indicators
    group_df['ADX'] = ta.trend.adx(group_df['High'], group_df['Low'], group_df['Close'])
    group_df['MACD'] = ta.trend.macd(group_df['Close'])
    group_df['MACD_Signal'] = ta.trend.macd_signal(group_df['Close'])

    # Momentum Indicators
    group_df['RSI'] = ta.momentum.rsi(group_df['Close'])
    group_df['Stochastic'] = ta.momentum.stoch(group_df['High'], group_df['Low'], group_df['Close'])
    group_df['ROC'] = ta.momentum.roc(group_df['Close'])

    # Volatility Indicators
    group_df['BB_upper'], group_df['BB_mid'], group_df['BB_lower'] = ta.volatility.bollinger_hband(group_df['Close']), \
        ta.volatility.bollinger_mavg(group_df['Close']), \
        ta.volatility.bollinger_lband(group_df['Close'])
    group_df['ATR'] = ta.volatility.average_true_range(group_df['High'], group_df['Low'], group_df['Close'])

    # Volume Indicators
    group_df['OBV'] = ta.volume.on_balance_volume(group_df['Close'], group_df['Volume'])
    group_df['CMF'] = ta.volume.chaikin_money_flow(group_df['High'], group_df['Low'], group_df['Close'], group_df['Volume'])

    print(f'Group: {group_name}\n group_df: \n{group_df}')

    if show_plotly:
        fig1 = go.Figure()
        # Moving Average Indicators
        close = go.Scatter(x=group_df.index, y=group_df.loc[:, 'Close'], mode='lines', name='Close')
        trace_ma_2 = go.Scatter(x=group_df.index, y=group_df.loc[:, 'SMA_2'], mode='lines', name='MA (10)')
        trace_ma_5 = go.Scatter(x=group_df.index, y=group_df.loc[:, 'SMA_5'], mode='lines', name='MA (50)')

        fig1.add_trace(close)
        fig1.add_trace(trace_ma_2)
        fig1.add_trace(trace_ma_5)

        # Show the plot
        fig1.update_layout(
            title='Moving Average Indicators',
            xaxis_title='Timestamp',
            yaxis_title='Value',
            xaxis=dict(tickangle=-45),
            showlegend=True
        )
        fig1.show()

        fig2 = make_subplots(rows=3, cols=1)

        close = go.Scatter(x=group_df.index, y=group_df.loc[:, 'Close'], mode='lines', name='ADX')
        trace_MACD = go.Scatter(x=group_df.index, y=group_df.loc[:, 'MACD'], mode='lines', name='MACD')
        trace_MACD_Signal = go.Scatter(x=group_df.index, y=group_df.loc[:, 'MACD_Signal'], mode='lines', name='MACD_Signal')
        trace_ADX = go.Scatter(x=group_df.index, y=group_df.loc[:, 'ADX'], mode='lines', name='MDX')

        fig2.add_trace(close, row=1, col=1)
        fig2.add_trace(trace_MACD, row=2, col=1)
        fig2.add_trace(trace_MACD_Signal, row=2, col=1)

        fig2.add_trace(trace_ADX, row=3, col=1)

        # Show the plot
        fig2.update_layout(
            title='Trend Indicators',
            xaxis_title='Timestamp',
            yaxis_title='Value',
            xaxis=dict(autorange=True),  # Automatically adjust x-axis range
            yaxis=dict(autorange=True),
            showlegend=True
        )
        fig2.show()

        #Momentum Indicators
        fig3 = make_subplots(rows=3, cols=1)

        close = go.Scatter(x=group_df.index, y=group_df.loc[:, 'Close'], mode='lines', name='ADX')
        trace_MACD = go.Scatter(x=group_df.index, y=group_df.loc[:, 'MACD'], mode='lines', name='MACD')
        trace_MACD_Signal = go.Scatter(x=group_df.index, y=group_df.loc[:, 'MACD_Signal'], mode='lines', name='MACD_Signal')
        trace_ADX = go.Scatter(x=group_df.index, y=group_df.loc[:, 'ADX'], mode='lines', name='MDX')

        fig3.add_trace(close, row=1, col=1)
        fig3.add_trace(trace_MACD, row=2, col=1)
        fig3.add_trace(trace_MACD_Signal, row=2, col=1)

        fig3.add_trace(trace_ADX, row=3, col=1)

        # Show the plot
        fig3.update_layout(
            title='Trend Indicators',
            xaxis_title='Timestamp',
            yaxis_title='Value',
            xaxis=dict(autorange=True),  # Automatically adjust x-axis range
            yaxis=dict(autorange=True),
            showlegend=True
        )
        fig3.show()

        counter += 1
        if counter == 1:
            break

if show_matplotlib:
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))
    plt.plot(df.loc['Timestamp'], df.loc['Close'], label='Close Price')
    #plt.plot(df.loc['Timestamp'], df.loc['ma_10'], label='MA 10')
    #plt.plot(df.loc['Timestamp'], df.loc['ma_50'], label='MA 50')
    plt.legend()
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.title('Price with Moving Averages')
    plt.show()

    plt.figure(figsize=(12, 4))
    plt.plot(df.loc['Timestamp'], df.loc['rsi'], label='RSI', color='red')
    plt.legend()
    plt.xlabel('Timestamp')
    plt.ylabel('RSI')
    plt.title('Relative Strength Index (RSI)')
    plt.show()

