################## IMPORT REQUIRED LIBRARIES ##################################
import requests
import re
import json
import tweepy
import pymongo
import numpy as np
import pandas as pd
import seaborn as sns
from pymongo import MongoClient

print("All libraries imported successfully")
print("********************************************************************************")
################## ALL API KEYS ##################################

""" Twitter API Keys
"""
consumer_key = "xxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxx"
access_token = "xxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxx"
auth = tweepy.OAuthHandler( consumer_key , consumer_secret )
auth.set_access_token( access_token , access_token_secret )
api = tweepy.API(auth)

print("Twitter API Key Authenticated")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------

""" Weather API Keys
"""
api_key = "xxxxxxxxxxxxxxxxxx"
api_url = "http://api.openweathermap.org/data/2.5/weather?"

print("Weather API Key Authenticated")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------

record_count = int(input("Enter the number of records you want to fetch: ")) # How much data needs to be pulled. 
print("********************************************************************************")
#-----------------------------------------------------------------------------------------------------------------


df_tweet = pd.DataFrame(columns=["user_id","date","user","screen_name","is_verified","tweet","likes","re_tweet",
                                 "location","language","followers_count","friends_count","listed_count","statuses_count",
                                 "favourites_count"])

print("Empty Data Frame Created with for Storing Twitter Data")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------

""" Defined an function to take the requests and store it into the dataframe. Different parameters are passed to extract 
    different variables from the API. I also encountered an trigger to stop the API calls and get only specified records 
    by using count variable. We will use api as api.search inside this tweepy cursor. We will Use **tweepy.cursor()** 
    because we want to extract a larger number of tweets i.e over 100,500 etc
"""

def get_tweets(topic,count):
    """ This function is triggred when an API call is made to twitter. Different values are stored in different
        variables as specified in the empty dataframe.
        
        count: Number of records to be fetched from the API
        topic: Key-words on which we have to generate data. In our case it will Starbucks
    """
    i=0
    for tweet in tweepy.Cursor(api.search, q=topic,count=100, lang="en",exclude='retweets').items():
        print("Tweets Count - ",i, end='\r')
        df_tweet.loc[i,"user_id"] = tweet.user.id # User ID
        df_tweet.loc[i,"date"] = tweet.created_at # Date
        df_tweet.loc[i,"user"] = tweet.user.name # User Name
        df_tweet.loc[i,"screen_name"] = tweet.user.screen_name # Screen Name
        df_tweet.loc[i,"is_verified"] = tweet.user.verified # User Verified or Not
        df_tweet.loc[i,"tweet"] = tweet.text # Tweet
        df_tweet.loc[i,"likes"] = tweet.favorite_count # Likes
        df_tweet.loc[i,"re_tweet"] = tweet.retweet_count # Retweet Count
        df_tweet.loc[i,"location"] = tweet.user.location # Location        
        df_tweet.loc[i,"language"] = tweet.lang # Language
        df_tweet.loc[i,"followers_count"] = tweet.user.followers_count # Follower Count
        df_tweet.loc[i,"friends_count"] = tweet.user.friends_count # Friends Count
        df_tweet.loc[i,"listed_count"] = tweet.user.listed_count # Listed Count
        df_tweet.loc[i,"statuses_count"] = tweet.user.statuses_count # Statues Count
        df_tweet.loc[i,"favourites_count"] = tweet.user.favourites_count #Favourites Count
        
        i=i+1
        if i>count:
            break
        else:
            pass
print("********************************************************************************")
""" Using "get_tweets" function we can call the API and store the data into dataframe. "count" variable specifies 
    number of records to be fetched and topic variable define which key words to be fetched.
"""

#-----------------------------------------------------------------------------------------------------------------

""" Weather Automation
"""

#-----------------------------------------------------------------------------------------------------------------

"""Created variables to store csv file path as well as storing the dataframe. Removed Nan Values from the dataframe.

locations_path: csv file path
locations_df: Dataframe containing world different locations 
countries_df: Dataframe containing specific countries
cities_df: Dataframe containing unique cities
"""
locations_path = (f"F:\\nci-projects\\starbucks-twitter-analysis\\datasets\\directory.csv")
locations_df = pd.read_csv(locations_path)
countries_df = locations_df[locations_df["Country"].isin(["AD","AE","AR","AT","AU","AW","AZ","BE","BG","BN","BO","BR","CA",
                                                       "CN","CO","CR","CW","CY","CZ","DE","DK","EG","ES","FI","FR","GB",
                                                       "GR","HU","ID","IE","IN","JP","KR","KW","KZ","LB","LU","MA","MX",
                                                       "NL","NO","PA","PE","PR","PT","QA","RO","RU","SA","SE","SG","SK",
                                                       "SV","TH","TR","TT","TW","US","VN","ZA"])]
countries_df = countries_df.dropna(axis = 0, how ='any')
cities_df = countries_df["City"].unique()
#-----------------------------------------------------------------------------------------------------------------


df = pd.DataFrame(columns=['city','latitude','longitude','temp_max','temp_min','avg_temp','pressure','humidity','cloud',
                           'wind_speed','wind_deg','country','date','sunrise','sunset','weather_status',
                           'weather_description'])

#-----------------------------------------------------------------------------------------------------------------

""" Defined an function to take the requests and store it into the dataframe. Different parameters are passed to extract 
    different variables from the API. I also encountered an trigger to stop the API calls and get only specified records 
    by using count variable.
"""
def weather_data(count):
    """ This function is triggred when an API call is made to openweathermap. Different values are stored in different
        variables as specified in the empty dataframe.
        
        count: Number of records to be fetched from the API
        query_url: Created URL by using API URL and API Key to access the data
        city_info: Fetch API and convert into JSON 
    """
    i = 0    
    for city in cities_df:
        print("Weather Data Count - ",i, end='\r')
        query_url = api_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        city_info = requests.get(query_url).json()
         
        try:
            city_info = requests.get(query_url).json()
            df.loc[i,'city'] = city_info["name"]
            df.loc[i,'latitude'] = city_info["coord"]["lat"]
            df.loc[i,'longitude'] = city_info["coord"]["lon"]
            df.loc[i,'temp_max'] = city_info["main"]["temp_max"]
            df.loc[i,'avg_temp'] = city_info["main"]["temp"]
            df.loc[i,'temp_min'] = city_info["main"]["temp_min"]
            df.loc[i,'pressure'] = city_info["main"]["pressure"]
            df.loc[i,'humidity'] = city_info["main"]["humidity"]
            df.loc[i,'cloud'] = city_info["clouds"]["all"]
            df.loc[i,'wind_speed'] = city_info["wind"]["speed"]
            df.loc[i,'wind_deg'] = city_info["wind"]["deg"]
            df.loc[i,'country'] = city_info["sys"]["country"]
            df.loc[i,'date'] = city_info["dt"]
            df.loc[i,'sunrise'] = city_info["sys"]["sunrise"]
            df.loc[i,'sunset'] = city_info["sys"]["sunset"]
            df.loc[i,'weather_status'] = city_info["weather"][0]["main"]
            df.loc[i,'weather_description'] = city_info["weather"][0]["description"]
            
        except(KeyError):
            print("")
        i=i+1
        if i > count:
            break
        else:
            pass

    print("Completed with Weather Data Collection")
print("********************************************************************************")
#-----------------------------------------------------------------------------------------------------------------

""" Getting Intraday data with the help of API is a challenge. I have created an function that can pull intraday data
    from IEX Cloud. Later, that will be stored in Dataframe and that will be imported in MongoDB Database. 
"""

def get_intraday_prices(symbol):
    """ This function stores the intraday data of the stock. "symbol" variable is passed to fetch the Starbucks Data.
        Creating an empty list of "Date", "Open", "Close", "High" and "Low" to append the values and store it in dataframe.
        After storing the values, "Matplotlib" Library is used to plot the graphs.  
    
    ticker: Stores symbol of Starbucks. ("SBUX")
    iex_api_key: API Key for IEX Cloud
    api_url: API URL for IEX Cloud
    df: Storing the data fetched in this variable
    date: Fetch current day data
    """
    ticker = symbol
    iex_api_key = "xxxxxxxxxxxxxxxxxx"
    url = f'https://cloud.iexapis.com/stable/stock/{ticker}/intraday-prices?token={iex_api_key}'
    df = requests.get(url).json()
    date = df[1]['date']
    
    dmy = []
    time = []
    open = []
    high = []
    low = []
    close = []
    volume = []
    number_of_trades = []
    
    for i in range(len(df)):
        dmy.append(df[i]['date'])
        time.append(df[i]['label'])
        open.append(df[i]['open'])
        high.append(df[i]['high'])
        low.append(df[i]['low'])
        close.append(df[i]['close'])
        volume.append(df[i]['volume'])
        number_of_trades.append(df[i]['numberOfTrades'])
        
    date_df = pd.DataFrame(dmy).rename(columns = {0:'date'})
    time_df = pd.DataFrame(time).rename(columns = {0:'time'})
    open_df = pd.DataFrame(open).rename(columns = {0:'open'})
    high_df = pd.DataFrame(high).rename(columns = {0:'high'})
    low_df = pd.DataFrame(low).rename(columns = {0:'low'})
    close_df = pd.DataFrame(close).rename(columns = {0:'close'})
    volume_df = pd.DataFrame(volume).rename(columns = {0:'volume'})
    number_of_trades_df = pd.DataFrame(number_of_trades).rename(columns = {0:'number_of_trades'})
     
    frames = [date_df, time_df, open_df, high_df, low_df, close_df, volume_df, number_of_trades_df]
    df = pd.concat(frames, axis = 1, join = 'inner')

    return df

#-----------------------------------------------------------------------------------------------------------------


plot_intraday = get_intraday_prices('SBUX')
intraday_df = pd.DataFrame(plot_intraday)

#-----------------------------------------------------------------------------------------------------------------

topic=["Starbucks","#starbucks"]
get_tweets(topic ,count=record_count)

#-----------------------------------------------------------------------------------------------------------------

""" Storing dataframe to CSV File.
"""

df_tweet.to_csv('{}.csv'.format("twitter-data-automate"),index=False)

#-----------------------------------------------------------------------------------------------------------------

""" Using "weather_data" function we can call the API and store the data into dataframe. "count" variable specifies 
    number of records to be fetched.
"""
weather_data(count=record_count)

#-----------------------------------------------------------------------------------------------------------------

""" Storing dataframe to CSV File.
"""
df.to_csv('{}.csv'.format("weather-data-automate"),index=False)

#-----------------------------------------------------------------------------------------------------------------


""" Storing dataframe to CSV File.
"""

intraday_df.to_csv('{}.csv'.format("intrday-data-automate"),index=False)

#-----------------------------------------------------------------------------------------------------------------

""" Importing the CSV File created into MongoDB Database.

file_path: CSV File Path Location
db: Creates a connection on localhost mongoDB with ports 27017
"""
twitter_file_path = (f"./twitter-data-automate.csv")
weather_file_path = (f"./weather-data-automate.csv")
intraday_file_path = (f"./intrday-data-automate.csv")

print("CSV for Twitter,Weather and Stocks CSV file created and stored in the folder")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------

db = MongoClient("mongodb://localhost:27017/")
print("Local database connected")
print("********************************************************************************")

cloud = MongoClient("mongodb+srv://admin:admin@cluster0.6eagf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
print("Cloud database connected")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------

def csv_to_json(filename, header=None):
    """This function converts the DataFrame(csv) into dictonary(document format[json]) which help to store the in MongoDB. 
    
    data: stores dataframe
    """
    data = pd.read_csv(filename, header=header)
    return data.to_dict('records')

db.twitter_database.tweeter_data_automate.insert_many(csv_to_json(twitter_file_path, header=0))

print("Your CSV file has been imported successfully in 'twitter_database' in 'tweeter_data_automate' collection")
print("********************************************************************************")
#-----------------------------------------------------------------------------------------------------------------

cloud.twitter_database.tweeter_data_automate.insert_many(csv_to_json(twitter_file_path, header=0))

print("Your CSV file has been imported successfully in 'twitter_database' in 'tweeter_data_automate' collection on MongoDB Atlas")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------

db.twitter_database.weather_automate.insert_many(csv_to_json(weather_file_path, header=0))
print("Your CSV file has been imported successfully in 'twitter_database' in 'weather_automate' collection")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------

cloud.twitter_database.weather_automate.insert_many(csv_to_json(weather_file_path, header=0))

print("Your CSV file has been imported successfully in 'twitter_database' in 'weather_automate' collection on MongoDB Atlas")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------
db.twitter_database.stock_data_automate.insert_many(csv_to_json(intraday_file_path, header=0))

print("Your CSV file has been imported successfully in 'twitter_database' in 'stock_data_automate' collection")
print("********************************************************************************")
#-----------------------------------------------------------------------------------------------------------------

cloud.twitter_database.stock_data_automate.insert_many(csv_to_json(intraday_file_path, header=0))

print("Your CSV file has been imported successfully in 'twitter_database' in 'stock_data_automate' collection on MongoDB Atlas")
print("********************************************************************************")

#-----------------------------------------------------------------------------------------------------------------
