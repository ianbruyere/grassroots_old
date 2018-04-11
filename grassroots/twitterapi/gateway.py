from django.conf import settings
import tweepy 
from tweepy import OAuthHandler

auth = OAuthHandler(settings.TWITTER.API_KEY,settings.TWITTER.CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER.ACCESS_TOKEN, settings.TWITTER.ACCESS_SECRET)

api = tweepy.API(auth)

