# Updating Twitter Stats using Tweepy
# Docs : https://github.com/tweepy/tweepy
import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")

import os
import getQuotes

# helps to load env values from .env files
# References : https://pypi.org/project/python-dotenv/
from dotenv import load_dotenv
load_dotenv()

# Set the various access codes
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

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
print("Successfully generated a tweet...")
# input('Press any key to exit...')