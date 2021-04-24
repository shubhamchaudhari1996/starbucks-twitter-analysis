# Yahoo Finance API
# import yfinance as yf
# sbux = yf.Ticker("SBUX")
# print(sbux.info)
# print(sbux.history(period="max"))

# iex-cloud
import pandas as pd
import requests
from termcolor import colored as cl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (15,8)

# def get_latest_updates(*symbols):
#     for i in symbols:
#         ticker = i
#         iex_api_key = 'pk_cdb21b0b9e3e47eebee0b70b6ee79876 '
#         api_url = f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={iex_api_key}'
#         df = requests.get(api_url).json()
#         print(cl('Latest Updates of {}\n--------------'.format(ticker), attrs = ['bold']))
#         attributes = ['symbol', 
#                       'latestPrice', 
#                       'marketCap', 
#                       'peRatio']
#         for i in attributes:
#             print(cl('{} :'.format(i), attrs = ['bold']), '{}'.format(df[i]))    
#         print(cl('--------------\n', attrs = ['bold']))

# get_latest_updates('SBUX')


def get_historic_data(symbol):
    ticker = symbol
    iex_api_key = 'Tsk_30a2677082d54c7b8697675d84baf94b'
    api_url = f'https://sandbox.iexapis.com/stable/stock/{ticker}/chart/max?token={iex_api_key}'
    df = requests.get(api_url).json()
    
    date = []
    open = []
    high = []
    low = []
    close = []
    
    for i in range(len(df)):
        date.append(df[i]['date'])
        open.append(df[i]['open'])
        high.append(df[i]['high'])
        low.append(df[i]['low'])
        close.append(df[i]['close'])
    
    date_df = pd.DataFrame(date).rename(columns = {0:'date'})
    open_df = pd.DataFrame(open).rename(columns = {0:'open'})
    high_df = pd.DataFrame(high).rename(columns = {0:'high'})
    low_df = pd.DataFrame(low).rename(columns = {0:'low'})
    close_df = pd.DataFrame(close).rename(columns = {0:'close'})
    
    frames = [date_df, open_df, high_df, low_df, close_df]
    df = pd.concat(frames, axis = 1, join = 'inner')
    df = df.set_index('date')
    
    df['open'].plot()
    plt.title('{} Historical Prices'.format(ticker), fontsize = 18)
    plt.xlabel('Date', fontsize = 14)
    plt.ylabel('Stock Price', fontsize = 14)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    plt.show()
    
    return df

get_historic_data('SBUX')