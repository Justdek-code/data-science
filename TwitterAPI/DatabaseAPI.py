import sqlite3
import json
import mysql.connector
from mysql.connector import Error
from Tweet import Tweet

class DatabaseAPI():

    def __init__(self, settings_json_path):
        self.settings_json_path = settings_json_path
        self.setup_database(settings_json_path)

    def setup_database(self, settings_path):
        self.connection: None

        with open(settings_path) as settings:
            settings = json.load(settings)
            host_name = settings['DATABASE_HOST_NAME']
            user_name = settings['DATABASE_USER_NAME']
            password = settings['DATABASE_PSWRD']
            self.database_name = settings['DATABASE_NAME']

            self.connection = self.create_connection(host_name, user_name, password)
            self.cursor = self.connection.cursor()

        self.create_database(self.database_name)
        self.create_table_tweets()


    def create_connection(self, host_name, user_name, user_password):
        connection = None

        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection


    def create_database(self, database_name):
        create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name};"
        select_database_query = f"USE {database_name};"

        try:
            self.cursor.execute(create_database_query)
            print("Database created successfully")
            self.cursor.execute(select_database_query)
            print(f"Database {database_name} selected")
        except Error as e:
            print(f"The error '{e}' occurred")


    def create_table_tweets(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS tweets (
                tweet_id VARCHAR(25) NOT NULL,
                publisher_id TEXT NOT NULL,
                tweet_text VARCHAR(350) NOT NULL,
                publisher_name VARCHAR(30) NOT NULL,
                datetime DATETIME NOT NULL,
                likes INT NOT NULL,
                retweets INT NOT NULL,
                hashtags TEXT DEFAULT NULL,
                PRIMARY KEY (tweet_id)
            );"""

        try:
            self.cursor.execute(create_table_query)
            print("table tweets is created successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def write_to_csv(self, filename):
        query = f"""SELECT *
                INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/{filename}'
                FIELDS TERMINATED BY ','
                ENCLOSED BY '"'
                LINES TERMINATED BY '\n'
                FROM tweets;"""
        
        try:
            self.cursor.execute(query)
            print("csv file is successfully created")
        except Error as e:
            print(f"The error '{e}' occurred")
            

    def write_tweet(self, tweet:Tweet):
        insert_tweet_query = f"""
            INSERT INTO tweets (tweet_id, tweet_text, publisher_name, datetime, likes, retweets, hashtags, publisher_id)
            VALUES ("{tweet.id_str}", "{tweet.content}", "{tweet.publisher_name}", "{tweet.date}", 
                {tweet.likes_count}, {tweet.retweets_count}, "{str(tweet.hashtags)}", "{tweet.publisher_id}");"""

        try:
            self.cursor.execute(insert_tweet_query)
            print("tweet is successfully inserted")
        except Error as e:
            print(f"The error '{e}' occurred")
        
        self.connection.commit()