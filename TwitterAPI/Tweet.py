import tweepy

class Tweet():

    def __init__(self, tweet):
        self.parse_tweet(tweet)

    def parse_tweet(self, tweet):
        self.publisher_name = tweet.user.name
        self.content = tweet.text
        self.likes_count = tweet.favorite_count
        self.retweets_count = tweet.retweet_count
        self.date = tweet.created_at

    def print_tweet_data(self):

        info = {
            'Publisher_name': self.publisher_name,
            'Content': self.content,
            'Likes': self.likes_count,
            'Retweets': self.retweets_count,
            'Date': self.date
        }

        for key, value in info.items():
            print(key, ': ', value)

        print(10 * '--')