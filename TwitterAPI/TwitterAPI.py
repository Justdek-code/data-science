import tweepy
import json
import os
from Tweet import Tweet
from DatabaseAPI import DatabaseAPI

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

# for tweet in public_tweets:
#     tweet = Tweet(tweet)
#     #database.write_tweet(tweet)
#     tweet.print_tweet_data()

userID = 'cz_binance'

tweets = api.user_timeline(screen_name=userID, 
    count=200,
    include_rts = False,
    tweet_mode = 'extended'
  )

all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id
while True:
  tweets = api.user_timeline(screen_name=userID, 
      count=200,
      include_rts = False,
      max_id = oldest_id - 1,
      tweet_mode = 'extended'
    )

  for tweet in tweets:
    tweet = Tweet(tweet)
    database.write_tweet(tweet)

  if len(tweets) == 0:
    break

  oldest_id = tweets[-1].id
  all_tweets.extend(tweets)
  print('N of tweets downloaded till now {}'.format(len(all_tweets)))