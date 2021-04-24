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

# cursor.execute("CREATE DATABASE starbucksdata")
cursor.execute("CREATE TABLE tweets (user_id BIGINT(255), user VARCHAR(255),screen_name VARCHAR(255),\
is_verified BOOL,likes INT(255),re_tweet INT(255),location VARCHAR(255),language VARCHAR(255),\
followers_count INT(255),friends_count INT(255),listed_count INT(255),statuses_count INT(255),\
favourites_count INT(255),day INT(255),month INT(255),year INT(255),\
clean_tweet VARCHAR(10000),sentiment VARCHAR(255))")

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)