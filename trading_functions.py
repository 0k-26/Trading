
#Imports 

import yfinance as yf
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def get_data(ticker_symbol): 
    '''
    Gets data for the ticker that we want for analysis

    Attributes: 
    ------------
    ticker (type: str)
        The name of the ticker you want for analysis (taken from yahoo finance)

    Returns: 
    ------------
    df (pandas dataframe)
        A dataframe of the closing prices of the required ticker 

    Notes: 
    ------------
    Author: Oliver Kelly
    Date: 04/07/2025
    '''
    ticker = yf.Ticker(ticker_symbol)
    
    df = ticker.history(period = "max")


    return df

def add_MA(df, WINDOW): 
    '''
    adds a moving average to the dataframe

    Attributes: 
    ------------
    WINDOW (type: int)
        amount of time the moving average is calculated from
    Returns: 
    ------------
    df (pandas dataframe)
        A dataframe of the Moving Average of the required ticker 

    Notes:
    ------------
    Author: Oliver Kelly
    Date: 04/07/2025
    '''
    ...
    df["MA"] = df['Close'].rolling(WINDOW).mean()

    return df

def add_RSI(df,WINDOW): 

    '''
    Calculates the Relative strength index (RSI) for the ticker 

    Attributes: 
    ------------
    WINDOW (type: int)
        amount of time the RSI is calculated from
    Returns: 
    ------------
    df (pandas dataframe)
        A dataframe of the RSI of the required ticker 

    Notes:
    ------------
    Author: Oliver Kelly
    Date: 04/07/2025
    '''
    # Delta
    delta = df['Close'].diff()
    # Gain
    gain = delta.where(delta>0,0)
    # Loss
    loss = abs(delta.where(delta < 0,0))

    avg_gain = gain.rolling(WINDOW).mean()
    avg_loss = loss.rolling(WINDOW).mean()

    rs = avg_gain/avg_loss

    df["RSI"] = 100 - (100 / (1+rs))


    return df




