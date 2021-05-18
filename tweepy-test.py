# Updating Twitter Stats using Tweepy
# Docs : https://github.com/tweepy/tweepy
import tweepy

import os
import getQuotes
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# helps to load env values from .env files
# References : https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
load_dotenv()

# Set the various access codes
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


def createQuoteTweet():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	# If the authentication was successful, you should
	# see the name of the account print out
	print("Logging in as :"+api.me().name)
	quote = getQuotes.getRandomQuote()
	print(quote)

	# If the application settings are set for "Read and Write" then
	# this line should tweet out the message to your account's
	# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
	api.update_status(status=quote)
	#input('Press any key to exit...')

sched.add_job(createQuoteTweet, "interval", minutes=240)
sched.start()
