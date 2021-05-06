import tweepy
from unidecode import unidecode
import re

class Tweet():

    def __init__(self, tweet):
        self.parse_tweet(tweet)

    def parse_tweet(self, tweet):
        self.publisher_name = self.remove_unnecessary_spaces(self.remove_non_ascii(tweet.user.name))
        self.likes_count = tweet.favorite_count
        self.retweets_count = tweet.retweet_count
        self.date = tweet.created_at
        self.id_str = tweet.id_str

        self.hashtags = self.parse_hashtags(tweet.entities['hashtags'])
        self.content = self.parse_content_text(tweet.full_text)
        self.screen_name = tweet.user.screen_name

        self.publisher_id = tweet.user.id_str


    def parse_hashtags(self, hashtags):
        result = list()
        
        for hashtag in hashtags:
            ascci_hashtag = self.remove_non_ascii(hashtag['text'])
            result.append(ascci_hashtag)

        return result


    def parse_content_text(self, content):
        replace_symbols = [
            ('\n', ''),
            ('\"', '\''),
            ('\r', ''),
            ('\t', ''),    
        ]   

        for old_symbol, new_symbol in replace_symbols:
            content = content.replace(old_symbol, new_symbol)

        content = self.remove_non_ascii(content)
        content = self.remove_links_from_text(content)
        content = self.remove_unnecessary_spaces(content)

        content = content.strip()

        return content


    def remove_non_ascii(self, text):
        return text.encode("ascii", "ignore").decode()


    def remove_links_from_text(self, text):
        return re.sub(r'http\S+', '', text)


    def remove_unnecessary_spaces(self, text):
        return text.replace(2 * ' ', ' ')


    def print_tweet_data(self):

        info = {
            'Publisher_name': self.publisher_name,
            'Content': self.content,
            'Likes': self.likes_count,
            'Retweets': self.retweets_count,
            'Date': self.date,
            'Hastags': self.hashtags,
            'Publisher Id': self.publisher_id
        }

        for key, value in info.items():
            print(key, ': ', value)

        print(30 * '=')