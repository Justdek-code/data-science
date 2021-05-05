import tweepy
import json
import os
from Tweet import Tweet
from DatabaseAPI import DatabaseAPI
from unidecode import unidecode

working_directory = os.getcwd()

settings_path = os.path.join(working_directory, 'TwitterAPI\settings.json')

APP_KEY: str()
APP_SECRET: str()
TOKEN: str()
TOKEN_SECRET: str()

with open(settings_path) as settings:
  settings = json.load(settings)
  APP_KEY = settings['APP_KEY']
  APP_SECRET = settings['SECRET_KEY']
  TOKEN = settings['ACCESS_TOKEN']
  TOKEN_SECRET = settings['ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline(count=50)

database = DatabaseAPI(settings_path)

for tweet in public_tweets:
    tweet = Tweet(tweet)
    database.write_tweet(tweet)

    tweet.print_tweet_data()
