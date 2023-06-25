from config import config
import tweepy
from tweepy import OAuthHandler

consumer_key = config["API_KEY"]
consumer_secret = config["CONSUMER_SECRET"]
access_token = config["ACCESS_TOKEN"]
access_secret = config["ACCESS_SECRET"]

print(consumer_key)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)