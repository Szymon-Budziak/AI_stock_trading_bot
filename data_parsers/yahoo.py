import yfinance as yf
import pandas as pd


def compute_diffs(data):
    average_price = (data["Open"] + data["Close"])/2
    data["average_price"] = average_price
    for interval in range(1, 3):
        data["diff_"+str(interval)] =\
            data["average_price"].pct_change(periods=interval)
    data["tomorrow"] = data["average_price"].pct_change(periods=-1)
    data.dropna(inplace=True)
    return data


def get_historical_data(name_of_token: str):
    token = yf.Ticker(name_of_token)
    info = token.info["longBusinessSummary"]
    data = token.history(period="max")
    data = data[["Open", "Close", "High", "Low"]]
    data = compute_diffs(data)
    print(data.head())
    return data
