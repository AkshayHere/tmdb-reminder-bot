# Updating Twitter Stats using Tweepy
# Docs : https://github.com/tweepy/tweepy
from dotenv import load_dotenv
import tweepy
import datetime

import os
from operator import attrgetter
import getQuotes
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# helps to load env values from .env files
# References : https://pypi.org/project/python-dotenv/
load_dotenv()

# Set the various access codes
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
CLIENT_KEY = os.getenv("CLIENT_KEY")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_ID = 1523585758510010368  # TESTING USER ID


def createQuoteTweet():
    print("Entering createQuoteTweet...")
    auth = tweepy.OAuth1UserHandler(consumer_key,
                                    consumer_secret, access_token, access_token_secret)
    # auth.set_access_token(access_token, access_token_secret)
    print("Defined tokens...")

    api = tweepy.Client(bearer_token, consumer_key,
                        consumer_secret, access_token, access_token_secret)

    # If the authentication was successful, you should
    # see the name of the account print out
    current_user = api.get_me()
    print(current_user)
    # print(dir(current_user))
    print(current_user.data)
    print(dir(current_user.data))
    id, username = attrgetter('id', 'username')(current_user.data)
    print('id : '+str(id))
    print('username : '+username)

    quote = getQuotes.getRandomQuote()
    print(quote)

    # If the application settings are set for "Read and Write" then
    # this line should tweet out the message to your account's
    # timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
    # api.update_status(status=quote)
    api.create_tweet(text=quote, user_auth=False)
    input('Press any key to exit...')


def getUserTimeline():
    client = tweepy.Client(bearer_token)
    tweets = client.get_users_tweets(id=USER_ID, tweet_fields=[
                                     'context_annotations', 'created_at', 'geo'])
    for tweet in tweets.data:
        print(tweet)


def sampleCreateTweet():
    client = tweepy.Client(consumer_key=consumer_key,
                           consumer_secret=consumer_secret,
                           access_token=access_token,
                           access_token_secret=access_token_secret)


    ct = datetime.datetime.now()
    # Replace the text with whatever you want to Tweet about
    parent_tweet = client.create_tweet(text=f'hello world {ct.timestamp()}')
    print(parent_tweet)
    print(parent_tweet[0])
    parent_data = parent_tweet[0]
    print(parent_data['id'])

    details_tweet = client.create_tweet(text='Check for more https://www.reuters.com/world/europe/ukraine-pledges-sweeping-personnel-changes-allies-jostle-over-tanks-2023-01-23/', in_reply_to_tweet_id=parent_data['id'])
    print(details_tweet)


# sched.add_job(createQuoteTweet, "interval", seconds=10)
# sched.start()
# createQuoteTweet()
sampleCreateTweet()
