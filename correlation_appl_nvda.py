import pandas as pd
import yfinance as yf
from datetime import datetime
import plotly.express as px

start_date = datetime.now() - pd.DateOffset(years=24)
end_date = datetime.now()

tickers = ['AAPL', 'NVDA']

df_list = []

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    df_list.append(data)

df = pd.concat(df_list, keys=tickers, names=['Ticker', 'Date'])
df = df.reset_index()

# create a DataFrame with the stock prices of Apple and Nvidia
Apple = df.loc[df['Ticker'] == 'AAPL', ['Date', 'Close']].rename(columns={'Close': 'AAPL'})
Nvidia = df.loc[df['Ticker'] == 'NVDA', ['Date', 'Close']].rename(columns={'Close': 'NVDA'})
df_corr = pd.merge(Apple, Nvidia, on='Date')

# create a scatter plot to visualize the correlation
fig = px.scatter(df_corr, x='AAPL', y='NVDA', 
                 trendline='ols', 
                 title='Correlation between Apple and Nvidia')
fig.show()