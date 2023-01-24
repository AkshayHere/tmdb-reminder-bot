# Updating Twitter Stats using Tweepy
# Docs : https://github.com/tweepy/tweepy
from dotenv import load_dotenv
import tweepy

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


def createQuoteTweet():
    print("Entering createQuoteTweet...")
    # auth = tweepy.OAuth1UserHandler(consumer_key,
    #                     consumer_secret, access_token, access_token_secret)
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


# sched.add_job(createQuoteTweet, "interval", seconds=10)
# sched.start()
createQuoteTweet()
