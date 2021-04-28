################## IMPORT REQUIRED LIBRARIES ##################################
import requests
import re
import nltk
import json
import folium
import sqlite3
import warnings
import mysql.connector
import tweepy
import pymongo
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
from pymongo import MongoClient
from mysql.connector import Error
pd.set_option('mode.chained_assignment', None)
warnings.filterwarnings("ignore")
from textblob import TextBlob
from tweepy import OAuthHandler
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
warnings.simplefilter(action="ignore", category=FutureWarning)
sns.set_style('whitegrid')

################## ALL API KEYS ##################################

# consumer_key = "xhsSu7y92oAFi9U3yX794Chav"
# consumer_secret = "0YWxdhZ2XvBs6Tk33iolwIYSdcuZL23CmhRK1TeHV6bIMdQ7SM"
# access_token = "324351622-rO9AGKtQ8WvWBQrX8bnWlEvXcJ3FgKpR3tPLB7fW"
# access_token_secret = "8OAe9FSFELuvIRHccwOgncxAgxIPgGvp19JDe44IeYOuV"
# auth = tweepy.OAuthHandler( consumer_key , consumer_secret )
# auth.set_access_token( access_token , access_token_secret )
# api = tweepy.API(auth)


client = pymongo.MongoClient("mongodb+srv://root:AI%40123@cluster0.6eagf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

