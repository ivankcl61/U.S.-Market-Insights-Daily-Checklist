import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib
# Use Agg backend for non-interactive plotting
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime

start_date = "2023-01-01"
yesterday = datetime.datetime.now()-datetime.timedelta(days=1)
end_date = yesterday.strftime("%Y-%m-%d")

tickers = ["^GSPC","^DJI","^IXIC","BTC-USD","ETH-USD",]

for ticker in tickers:
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.to_csv(f"{ticker}_historical_data.csv")

    stock_df = pd.read_csv(f"{ticker}_historical_data.csv")

    stock_df["Open"] = pd.to_numeric(stock_df["Open"], errors='coerce')
    stock_df["Close"] = pd.to_numeric(stock_df["Close"], errors='coerce')
    stock_df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
    stock_df.drop(index=[0, 1], inplace=True)
    stock_df["Date"] = pd.to_datetime(stock_df["Date"])

    x=stock_df["Date"]
    y=stock_df["Close"]

    plt.plot(x,y)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(ticker)
    plt.savefig(f"{ticker}.png")
    plt.close()

