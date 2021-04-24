# 1. Import Libraries

import json
import pymongo
import tweepy
import re
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from tweepy import OAuthHandler
from pymongo import MongoClient


# Importing Dataset to MongoDB
db = MongoClient("mongodb://localhost:27017/")
database = db["twitter_database"] # collection instance

# Exporting Data from MongoDB
collection = database["tweeter_data"]
twitter_dataset = collection.find()

df_twitter = pd.DataFrame(list(twitter_dataset))

df_twitter = df_twitter[["user_id","date","user","screen_name","is_verified","tweet","likes","re_tweet","location","language","followers_count","friends_count","listed_count","statuses_count","favourites_count"]]

df_twitter_clean = df_twitter.dropna()
# print("-----------------------------------------------------------------------------")
# print("Original - USA",df_twitter_clean.loc[df_twitter_clean['location'] == 'USA'].shape[0])
# print("-----------------------------------------------------------------------------")
# print("Original - UK",df_twitter_clean.loc[df_twitter_clean['location'] == 'UK'].shape[0])
# print("-----------------------------------------------------------------------------")
# print("Original - New York",df_twitter_clean.loc[df_twitter_clean['location'] == 'New York'].shape[0])
# print("-----------------------------------------------------------------------------")

countries = ["UK","USA","New York"]
location_df = pd.DataFrame()
for i in countries:
#     print(i)
    filter_loc = pd.DataFrame(df_twitter_clean.loc[df_twitter_clean['location'] == i])
    location_df = location_df.append(filter_loc)
# print("-----------------------------------------------------------------------------")
# print("After Loop Filter on Countries -", location_df.shape[0])
# print("-----------------------------------------------------------------------------")
# print("New - USA",location_df.loc[location_df['location'] == 'USA'].shape[0])
# print("-----------------------------------------------------------------------------")
# print("New - UK",location_df.loc[location_df['location'] == 'UK'].shape[0])
# print("-----------------------------------------------------------------------------")
# print("New - New York",location_df.loc[location_df['location'] == 'New York'].shape[0])
# print("-----------------------------------------------------------------------------")

# Reset our index so datetime_utc becomes a column
# disable chained assignments
pd.options.mode.chained_assignment = None 

location_df.reset_index(inplace=True)
location_df['date'] = pd.to_datetime(location_df['date'], errors='coerce')
# Create new columns

location_df['day'] = location_df['date'].dt.month
# print(location_df['month'])
# print("-----------------------------------------------------------------------------")

location_df['month'] = location_df['date'].dt.day
# print(location_df['day'])
# print("-----------------------------------------------------------------------------")

location_df['year'] = location_df['date'].dt.year
# print(location_df['year'])
# print("-----------------------------------------------------------------------------")

location_df['time'] = pd.to_datetime(location_df['date'], format='%Y:%M:%D').dt.time
# print(location_df['time'])
# print("-----------------------------------------------------------------------------")

# print(location_df.head(5))

def clean_tweet(tweet):
    
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([RT])', ' ', str(tweet).lower()).split())

# We only want the Text so :

# (@[A-Za-z0-9]+)   : Delete Anything like @hello @Letsupgrade etc
# ([^0-9A-Za-z \t]) : Delete everything other than text,number,space,tabspace
# (\w+:\/\/\S+)     : Delete https://
# ([RT]) : Remove "RT" from the tweet

# Funciton to analyze Sentiment

#Function to Pre-process data for Worlcloud:here we are removing the words present in Topic from the Corpus so they dont come in WordCloud.
# Ex : Topic is "Arsenal vs United", we want to remove "Arsenal" "vs" "United" from the WordCloud.

def prepCloud(Topic_text,Topic):
    Topic = str(Topic).lower()
    Topic=' '.join(re.sub('([^0-9A-Za-z \t])', ' ', Topic).split())
    Topic = re.split("\s+",str(Topic))
    stopwords = set(STOPWORDS)
    stopwords.update(Topic) ### Add our topic in Stopwords, so it doesnt appear in wordClous
    ###
    text_new = " ".join([txt for txt in Topic_text.split() if txt not in stopwords])
    return text_new

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'


location_df['clean_tweet'] = location_df['tweet'].apply(lambda x : clean_tweet(x))

# Call function to get the Sentiments
location_df["sentiment"] = location_df["tweet"].apply(lambda x : analyze_sentiment(x))

# print(location_df.head(5))

# Overall Summary
print("-----------------------------------------------------------------------------")
print("Total Positive Tweets are : {}".format(len(location_df[location_df["sentiment"]=="Positive"])))
print("Total Negative Tweets are : {}".format(len(location_df[location_df["sentiment"]=="Negative"])))
print("Total Neutral Tweets are : {}".format(len(location_df[location_df["sentiment"]=="Neutral"])))
print("-----------------------------------------------------------------------------")

# Filtering by days
df_day = location_df.loc[location_df['day'] == 9]

# Overall Summary
# print("-----------------------------------------------------------------------------")
# print("Total Positive Tweets are : {}".format(len(df_day[df_day["sentiment"]=="Positive"])))
# print("Total Negative Tweets are : {}".format(len(df_day[df_day["sentiment"]=="Negative"])))
# print("Total Neutral Tweets are : {}".format(len(df_day[df_day["sentiment"]=="Neutral"])))
# print("-----------------------------------------------------------------------------")

# Filtering by months
df_month = location_df.loc[location_df['month'] == 4]

# Overall Summary
# print("-----------------------------------------------------------------------------")
# print("Total Positive Tweets are : {}".format(len(df_month[df_month["sentiment"]=="Positive"])))
# print("Total Negative Tweets are : {}".format(len(df_month[df_month["sentiment"]=="Negative"])))
# print("Total Neutral Tweets are : {}".format(len(df_month[df_month["sentiment"]=="Neutral"])))
# print("-----------------------------------------------------------------------------")

# Filtering by years
df_year = location_df.loc[location_df['year'] == 2021]

# Overall Summary
# print("-----------------------------------------------------------------------------")
# print("Total Positive Tweets are : {}".format(len(df_year[df_year["sentiment"]=="Positive"])))
# print("Total Negative Tweets are : {}".format(len(df_year[df_year["sentiment"]=="Negative"])))
# print("Total Neutral Tweets are : {}".format(len(df_year[df_year["sentiment"]=="Neutral"])))
# print("-----------------------------------------------------------------------------")

# Filtering by location and Day
df_loc = location_df.loc[location_df['location'] == 'New York']
df_loc_day = df_loc.loc[df_loc['day'] == 9]

# print(df_loc_day)
# Overall Summary
print("-----------------------------------------------------------------------------")
print("Total Positive Tweets are : {}".format(len(df_loc_day[df_loc_day["sentiment"]=="Positive"])))
print("Total Negative Tweets are : {}".format(len(df_loc_day[df_loc_day["sentiment"]=="Negative"])))
print("Total Neutral Tweets are : {}".format(len(df_loc_day[df_loc_day["sentiment"]=="Neutral"])))
print("-----------------------------------------------------------------------------")

####################################################################################################################

import mysql.connector
import sqlite3

print("-----------------------------------------------------------------------------")
def create_connection(hostname, username, userpass):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = userpass,
            database = "starbucksdata",
            auth_plugin='mysql_native_password'
        )
        print("MySQL Database Connected")
    except Error as err:
        print(f"Error:'{err}'")
    return connection

from mysql.connector import Error
pw = "AI@123"
connection = create_connection("127.0.0.1","root",pw)
cursor = connection.cursor()

columns = ["user_id","user","screen_name","is_verified","likes","re_tweet","location",
"language","followers_count","friends_count","listed_count","statuses_count","favourites_count",
"day","month","year","clean_tweet","sentiment"]

df_data = location_df[columns]
df_data = pd.DataFrame(df_data)

# creating column list for insertion
cols = "`,`".join([str(i) for i in df_data.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in df_data.iterrows():
    sql = "INSERT INTO `tweets` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    connection.commit()