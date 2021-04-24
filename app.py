import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

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

db = MongoClient("mongodb://localhost:27017/")
database = db["twitter_database"] # collection instance

collection = database["tweeter_data"]
twitter_dataset = collection.find()
df_twitter = pd.DataFrame(list(twitter_dataset))
df_twitter = df_twitter[["user_id","date","user","screen_name","is_verified","tweet","likes","re_tweet","location","language","followers_count","friends_count","listed_count","statuses_count","favourites_count"]]
df_twitter_clean = df_twitter.dropna()

countries = ["UK","USA","New York"]
location_df = pd.DataFrame()
for i in countries:
    filter_loc = pd.DataFrame(df_twitter_clean.loc[df_twitter_clean['location'] == i])
    location_df = location_df.append(filter_loc)

pd.options.mode.chained_assignment = None 

location_df.reset_index(inplace=True)
location_df['date'] = pd.to_datetime(location_df['date'], errors='coerce')
location_df['day'] = location_df['date'].dt.month
location_df['month'] = location_df['date'].dt.day
location_df['year'] = location_df['date'].dt.year
location_df['time'] = pd.to_datetime(location_df['date'], format='%Y:%M:%D').dt.time

def clean_tweet(tweet):
    
    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([RT])', ' ', str(tweet).lower()).split())

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
location_df["sentiment"] = location_df["tweet"].apply(lambda x : analyze_sentiment(x))
days = np.sort(location_df.day.unique())

app = dash.Dash(__name__)

app.layout = html.Div(children = 
                     [
                        html.H1("Starbucks Analysis",
                              style={'height':'5%','width':'30%', 'display':'inline-block'}),
                        html.H2('National College of Ireland'),                         
                        html.Label("Day"),
                        dcc.Dropdown(
                            id="dropdown",
                            options=[{"label": x, "value": x} for x in days],
                            value=days[0],
                            clearable=False,
                            style={'height':'10%', 'width':'20%','display':'inline-block'} 
                        ),
                        dcc.Graph(id="bar-chart",
                        style={'height':'20%','width':'40%'}),
                    ]
)

# app.layout = html.Div(children=
#                       [
#                           html.H1("Ecommerce Website Sales Dashboard for 2018-20",
#                                  style={'height':'5%','width':'60%', 'display':'inline-block'}),
#                           html.H2('(Top Selling Electronic Products)'),
                           
#                           html.Label("Categories"),
#                           dcc.Dropdown(id = 'Dropdown1',
#                                        options = options1,
# #                                        value = options1[0:],
#                                        placeholder = 'All',
#                                        style={'height':'30%', 'width':'40%','display':'inline-block'} ),
#                           dcc.Slider(id ='Slider1',
#                                     min =flat3['Year'].min(),
#                                     max=flat3['Year'].max(),
#                                     value=flat3['Year'].min(),
#                                     marks={str(i):str(i) for i in flat3['Year'].unique()},
# #                                      tooltip placement= 'topRight']
# #                                      style={'height':'30%','width':'20%', 'display':'inline-block'}
#                                     ),
#                           dcc.Graph(id = 'Graph1',figure = fig1,
#                                    style={'height':'40%','width':'40%', 'display':'inline-block'}),
#                           dcc.Graph(id = 'Graph2',figure = fig2,
#                                    style={'height':'60%','width':'30%', 'display':'inline-block'}),
#                           dcc.Graph(id = 'Graph3',figure = fig3,
#                                     style={'height':'40%','width':'30%', 'display':'inline-block'}),
#                           dcc.Graph(id = 'Graph4',figure = fig4,
#                                     style={'height':'100%','width':'100%'})
#                       ]
                                  
# )


@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(day):
    mask_day = location_df["day"] == day
    fig_day = px.bar(location_df[mask_day], x="sentiment", 
                 color="sentiment", barmode="group")
    return fig_day

if __name__ == "__main__":
    app.run_server(debug=True)
