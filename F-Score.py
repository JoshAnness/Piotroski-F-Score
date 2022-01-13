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
    balanceSheet = stock.balance_sheet
    cashFlow = stock.cashflow
    dfFin = pd.DataFrame(financials)
    dfBs = pd.DataFrame(balanceSheet)
    dfCf = pd.DataFrame(cashFlow)
    NI = dfFin.iloc[4][0]
    totalAssets = dfBs.iloc[3][0]
    ROA = NI / totalAssets
    OI = dfFin.iloc[8][0]
    CF = dfCf.iloc[10][0]
    LTD0 = dfBs.iloc[20][0]
    LTD1 = dfBs.iloc[20][1]
    CR0 = (dfBs.iloc[3][0]) / (dfBs.iloc[0][0])
    CR1 = (dfBs.iloc[3][1]) / (dfBs.iloc[0][1])
    CS0 = dfBs.iloc[4][0]
    CS1 = dfBs.iloc[4][1]

    print(stock.balance_sheet)
    print(CS0)
    print(CS1)

    return dfFin

df = getData("AAPL")
