import sqlite3
import json
from sqlite3 import Error

class DatabaseAPI():

    def __init__(self, settings_json_path):
        self.settings_json_path = settings_json_path
        self.setup_database(settings_json_path)

    def setup_database(self, settings_path):
        with open(settings_path) as settings:
            settings = json.load(settings)
            self.database_path = settings['DATABASE_PATH']

        self.connection = self.create_connection(self.database_path)

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def write_tweet(self, tweet):
        pass