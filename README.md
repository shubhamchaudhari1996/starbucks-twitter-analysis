<h1><center>Analysis of Twitter Sentiment and Weather Conditions on Starbucks Store Locations, along with Starbucks Stock Price Forecasting</center></h1>


![alt text](https://www.freepnglogos.com/uploads/starbucks-logo-png-1.png)


## Project Group Details
<b>Group Number</b> - 10
 
<b>Student Name:</b> Shubham Sarjerao Chaudhari<br>
<b>Student ID:</b> x20160836<br>
<b>Student Email ID:</b> x20160836@student.ncirl.ie <br>

<b>Student Name:</b> Vrushali Atul Surve<br>
<b>Student ID:</b> x19212712<br>
<b>Student Email ID:</b> x19212712@student.ncirl.ie <br>

<b>Student Name:</b> Shital Namdeo Raut<br>
<b>Student ID:</b> x19243294<br>
<b>Student Email ID:</b> x19243294@student.ncirl.ie <br>

<b>Subject:</b>Database and Analytics Programming<br>
<b>Lecturer:</b> Athanasios Staikopoulos<br>
<b>College:</b> National College of Ireland


## Introduction

Choosing a new location for a coffee shop or a food restaurant is a costly endeavor and can prove risky in business if factors like population, sales, nearby industries, and entire human flow are not considered or mis calculated. The main aim of this project is to study 4 different aspects related to Starbucks Store and those are Starbucks Store Locations, Twitter Sentiments regarding Starbucks stores, Climate, and the Stocks. The motivation behind choosing these factors is to study and analyze climatic factors and public sentiments that affect existing Starbucks store’s locations and their stock prices. In this study, significant factors are highlighted which could affect store’s locations and revenue. To handle computational constraints, a mix of locations were taken into consideration aiming to include regions from USA and European countries. The study enabled us to understand the extent to which weather influences store locations as well as impact of social media such as twitter on economic conditions of stores. Previous research into the economic state of coffee shop locations sparked people's interest in the relationship between sentiment analysis and climatic impacts. In this study we are using Python as a main programming language to parse JSON and CSV data containing Starbucks store’s locations along with twitter sentiments and weather description for respective store locations. Initially these data will be in semi structured format and Mongo DB will be used to store these data. Semi structured data will be converted into structured data using python and we will use SQL DB to store structured data. Structured data will get fetched using python to further visualize and analyze the data. From our analysis we aim to see majorly affected Starbucks store’s locations by twitter comments and need to observe weather conditions in that locations. Data analysis employed in this study is integral so that it can help customers to understand climate and reviews of Starbucks locations by looking at this data and employed strategies. We are hoping to see if data analysis will provide a better image of what we can see through our eyes. 

## Dataset Used
<b>1. Starbucks Store Location <br> 
2. Weather Data <br>
3. Starbucks Twitter Sentiment Data <br>
4. Starbucks Stocks Data </b>

## Dataset Descriptions

### 1. Starbucks Store Location (Vrushali Atul Surve)

![alt text](https://www.freepnglogos.com/uploads/starbucks-logo-png-1.png)

Investigate the Starbucks Store catalog in look for answers to following question.
<b>
* What country or city has the most Starbucks?
* We will likewise investigate the inquiry on the contrast between a Starbucks at Target and a Franchise-Store Starbucks
* What number of each kind are there? <br> </b> At last, we will end our investigation, by plotting each store on a Map utilizing folium <br>

#### A Brief History of Starbucks

Initially founded by Jerry Baldwin, Zev Siegl, and Gordon Bowker in 1971, Starbucks opened its first store at 1912 Pike's Place in Seattle, Washington. The future CEO, Howard Schultz joined with the young company in 1982 as the Director of Retail Operations & Marketing. In 1983, Schultz took his revolutionary trip across Italy, where fell in love with the concept of a "coffeehouse". Returning to the United States at the beginning of 1984, he explains the coffeehouse concept to the owner's, and convinces them to give it a try. The first Cafe Latte was sold later that year. After the coffeehouse experiment's success, Shultz stepped away from Starbuck's and founded II Giornale ,"The Jounal". 

From 1985-1987, Il Giornale grew substantially, and at the end of 1987 acquired the Starbuck's shop on Pike's Place. The acquisition then formed, what we know today as the Starbuck's Corporation. Before the end of 1987, there were 17 Starbucks Coffeehouses in cities such as Chicago, Vancouver, and Seattle. In 30 years, Starbuck's went from only 33 stores in 1988 to 25,600 stores worldwide.

### 2. Weather Data (Shital Namdeo Raut)

![alt text](https://upload.wikimedia.org/wikipedia/commons/f/f6/OpenWeather-Logo.jpg)

Investigate the Weather Location Data Analysis in look for objectives as follows.
<br>
<b>
* Create a DataFrame from an API search with weather parameters.
* Filter DataFrames based on input and nested decision statements, and logical expressions.
* Exploratory Data Analysis for Weather Data
</b>

#### Brief about Weather Location Data Analysis

The Daily Climate change has been a serious topic this year. The goal of this project was to analyze weather data related to maximum temperature, humidity, wind speed, and cloudiness for randomly selected global cities. Since the baseline data was collected from the Open Weather Map API, Python with Numpy, Citipy, Requests, Pandas, and Matplotlib was used to extract and process the data, as well as display the desired outputs.<br>

The current weather would be the use of scientific techniques and technologies to determine atmospheric conditions at a particular region and timeframe. Just like internal measures, Starbucks has used AccuWeather real-feel weather measures to analyze the weather (around one week in advance). they calculate which areas the weather would be super-hot, and they know that some people like cool beverages on hot days.

Though psychological is strongly claimed that the weather affects the behavior of a human being, there have been debates about their interrelationships for a long time. Data collected from available social media government climatology gateways by various weather prediction researchers in this survey are gathered from different prediction protocols.

### 3. Starbucks Twitter Sentiment Data (Shubham Sarjerao Chaudhari)

![alt text](https://icon-library.com/images/twitter-text-icon/twitter-text-icon-11.jpg)

Investigate the Weather Location Data Analysis in look for objectives as follows.
<br>
<b>
* Create a DataFrame from an API search with weather parameters.
* Filter DataFrames based on input and nested decision statements, and logical expressions.
* Exploratory Data Analysis for Weather Data
</b>

#### Brief about Starbucks Twitter Sentiment Analysis

Twitter is a social networking and microblogging site where people share and communicate with tweets. The significant increase in the number of social network users has given the opportunity to forecast the response of chosen public associations in wide-ranging fields. Nowadays, people spoke about being on the social network due to the rise of technology, including articles, the sharing of images and the streaming of videos. Twitter has been among the major sources of public opinion on different things affecting businesses, services, films and more. One of the measures for the stock price is the demand and the behavior of customers would have an important market effect. 

The market feeling about an enterprise and its goods is usually proportional to its actions at stock price. Place also has a major social network component, and the feeling of the location may be an indication of the price behavior of the stock. There was no work to correlate the feelings of a certain position that influence the stock behavior of a firm. A prototype framework was applied to locate the associations between Twitter's geographical feelings and stock price using Naive Bayes. This process allowed us to gather, interpret, and correlate the feelings of geographic knowledge based on tweets and the geographic feeling with company stock prices.

These tweets frequently share views on a variety of subjects. Analysis of the feelings is the analysis of emotions in the text or in the term. Twitter is a big forum and a powerful repository of unorganized and opinion datasets that can be analyzed to generate trending feelings and several other things. We inspect or mine any tweet factor in Twitter sentiment analysis. Just several substances and spots are the metadata of tweet. The article contains hashtags, URLs, media users and Twitter account id. All substances have a client. RT stands for retweet, '@' for customer data, and '#' for a word is a hashtag.

### 4. Starbucks Stocks Data (Shubham Sarjerao Chaudhari)
 
![alt text](https://miro.medium.com/max/600/0*oSQC-_PkXNZ-0mfI.png)

The weather has a great influence on people's feelings and behaviors. utilizing forecast data Weather is hardly provided responsibility with the ups and downs of the stock market. Researchers also found links between the financial market and other more boring facets of the weather. Professional analysts weigh a company's earnings, cash flow, executive staff, business environment, market trends, and economic growth rate when deciding how to value stocks. These variables are known as fundamentals, and they are generally acknowledged to play important roles in the success of a stock. What is most important for you is to construct and invest in a diversified selection that can withstand a hurricane, whether physical or metaphorical.


* <b>What is IEX Cloud?</b><br>

IEX Cloud is an easy-to-use financial data platform that makes a wide range of data accessible in one place. We built IEX Cloud to make financial data accessible to everyone, from individual developers to large businesses.  

Get stock prices, fundamentals, forex data, crypto data, and more all through a single API and a single IEX Cloud subscription, with flexible plans designed to fit your use case.


### Analysis Apporach 
Here I used PPDAC Apporach for my analysis <br>
A cycle that is used to carry out a statistical investigation. The cycle consists of five stages: Problem, Plan, Data, Analysis, Conclusion. The cycle is sometimes abbreviated to the PPDAC cycle.
<b>
* The problem section is about formulating a statistical question, what data to collect, who to collect it from and why it is important.
* The plan section is about how the data will be gathered.
* The data section is about how the data is managed and organised.
* The analysis section is about exploring and analysing the data, using a variety of data displays and numerical summaries, and reasoning with the data.
</b>
The conclusion section is about answering the question in the problem section and giving reasons based on the analysis section.

<br>

![alt text](https://dataschools.education/wp-content/uploads/2020/08/PPDAC-Spiral.png)

### Analysis Steps for all the Projects:
<br>
<b>
    1. Data Collection <br>
    2. Storing of Data in MongoDB <br>
    3. Retriving Data from MongoDB for further analysis <br>
    4. Data Exploration and Preparation <br>
    5. Missing Value Treatment <br>
    6. Data Visualisation <br>
    7. Results and Conclusions <br>
    8. Storing Data in SQL Database <br>
</b>

## Cloud Integration

![alt text](https://miro.medium.com/max/600/1*UniTjL05TA-vkvMXJFRdFg.png)

We hosted our database on cloud using MongoDB Atlas. We chose MongoDB Atlas as it provides amazing features including periodic backups. It also ensures stability of critical development databases by providing recovery in moment of time. We hosted a database named “twitter_databse” on Atlas and 4 data collections “location”,” stock_data”,” twitter_data” and “weather” were deployed on MongoDB Atlas using python scripting.

## Folder Structure

1. <b>automation</b> - Contains Automation File
2. <b>combined-project</b> - Contains Merged Dataset and Analysis File
3. <b>datasets</b> - Contains Datasets Files (Backup)
4. <b>reserach-papers</b> - Contains refered research papers
5. <b>starbucks-location-analysis</b> - Contains Location Analysis Files
6. <b>stock-analysis</b> - Contains Stock Analysis Files
7. <b>twitter-sentiment-analysis</b> - Contains Twitter Sentiment File
8. <b>weather-analysis</b> - Contains Weather Analysis File

## Installation Mandate
* pip install -r requirements.txt 

## Run Files

1. <b>automation-file.py</b> - Run automation-file.py and will asked to enter records needed to fetch from different API. Enter the number and that many records will be collected. This file will collect data from Twitter API, Weather API, and Stock API. It will also create csv file in the folder and create MongoDB Database at the local system and in Mongo Atlas.

2. <b>combined-research.ipynb</b> - Run this file to see Exploratory Data Analysis of merged datasets.

3. <b>x19212712-Vrushali-Surve-stabucks-location-analysis.ipynb</b> -  Run this file to see Exploratory Data Analysis of Starbucks Location.

4. <b>x20160836-shubham-chaudhari-stock-analysis.ipynb</b> -  Run this file to see Exploratory Data Analysis of Starbucks Stocks.

5. <b>x20160836-shubham-chaudhari-starbucks-twitter-analysis.ipynb</b> - Run this file to see Exploratory Data Analysis of Starbucks Sentiment Analysis.

6. <b>x19243294-shital-raut-weather-locations-analysis.ipynb</b> - - Run this file to see Exploratory Data Analysis of Weather Analysis.


## Special Thanks - Athanasios Staikopoulos
