import tweepy
import json
import os

working_directory = os.getcwd()

settings_path = os.path.join(working_directory, 'TwitterAPI\settings.json')
APP_KEY, APP_SECRET, TOKEN, TOKEN_SECRET = [str() for n in range(4)]

with open(settings_path) as settings:
  settings = json.load(settings)
  APP_KEY = settings['APP_KEY']
  APP_SECRET = settings['SECRET_KEY']
  TOKEN = settings['ACCESS_TOKEN']
  TOKEN_SECRET = settings['ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)