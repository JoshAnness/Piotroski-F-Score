import requests
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import yfinance as yf

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}

def getData(ticker):
    companyName = yf.Ticker(ticker)
    companyName = companyName.info['shortName']
    c = companyName.split(" ")
    url = 'https://www.macrotrends.net/stocks/charts/' + ticker.upper() + '/' + c[0] + '/roa'
    response = Request(url, headers = headers)
    webpage = urlopen(response).read()
    table = pd.read_html(webpage, match='Return on Assets Historical Data')
    df = pd.DataFrame(np.concatenate(table))
    df.columns = ['Date', 'TTM Net Income', 'Total Assets', 'Return on Assets']

    return df

def getROA(df):
    roa = df.iloc[0]['Return on Assets']
    roa = float(roa.strip('%'))
    if roa > 0:
        return 1
    else:
        return 0

def changeInROA(df):
    roa = df.iloc[0]['Return on Assets']
    roaOld = df.iloc[1]['Return on Assets']
    roa = float(roa.strip('%'))
    roaOld = float(roaOld.strip('%'))
    if roa > roaOld:
        return 1
    else:
        return 0
