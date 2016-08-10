from yelpapi import YelpAPI
import pprint
import os

# Accesses keys & tokens from Yelp that are securely set in environment
consumer_key = os.environ['YELP_CONSUMER_KEY']
consumer_secret = os.environ['YELP_CONSUMER_SECRET']
token = os.environ['YELP_ACCESS_TOKEN_KEY']
token_secret = os.environ['YELP_ACCESS_TOKEN_SECRET']

yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)

# Give yelp the lat/long and time preference from user form submit

# Query Yelp for yums based on those preferences

# Return the yums in a format (callback)?