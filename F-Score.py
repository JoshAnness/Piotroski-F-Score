import requests
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import yfinance as yf

def getData(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials
    df = pd.DataFrame(financials)
    NI = df.iloc[4][0]

    return df

df = getData("AAPL")
df.head()
