import sqlite3
import json
import mysql.connector
from mysql.connector import Error

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
                tweet_id INT NOT NULL AUTO_INCREMENT,
                tweet_text VARCHAR(350) NOT NULL,
                publisher_name VARCHAR(30) NOT NULL,
                datetime DATETIME NOT NULL,
                likes INT NOT NULL,
                retweets INT NOT NULL,
                PRIMARY KEY (tweet_id)
            );
            """
        try:
            self.cursor.execute(create_table_query)
            print("table tweets created successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
        

    def write_tweet(self, tweet):
        pass