from config import config
import tweepy
import tweepy
import logging

consumer_key = config["API_KEY"]
consumer_secret = config["CONSUMER_SECRET"]
access_token = config["ACCESS_TOKEN"]
access_secret = config["ACCESS_SECRET"]
bearer_token = config["BEARER_TOKEN"]
client_id = config["CLIENT_ID"]
client_secret = config["CLIENT_SECRET"]

print(consumer_key)
print(consumer_secret)

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_secret)

logging.basicConfig(level=logging.DEBUG)

client.get_users_tweets(id="469761474", max_results = 10, user_auth = True)