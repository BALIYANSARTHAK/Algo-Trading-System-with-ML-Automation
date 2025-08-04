import yfinance as yf
import pandas as pd

def download_data(ticker, period="6mo"):
    df = yf.download(ticker, period=period, auto_adjust=True)

    df.dropna(inplace=True)
    return df

def add_indicators(df):
    df['20DMA'] = df['Close'].rolling(window=20).mean()
    df['50DMA'] = df['Close'].rolling(window=50).mean()
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df