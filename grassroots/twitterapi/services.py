from django.conf import settings
import tweepy 
from tweepy import OAuthHandler, TweepError
from .serializers import StatusSerializer

auth = OAuthHandler(settings.TWITTER['API_KEY'], settings.TWITTER['CONSUMER_SECRET'])
auth.set_access_token(settings.TWITTER['ACCESS_TOKEN'], settings.TWITTER['ACCESS_SECRET'])

api = tweepy.API(auth)

def get_twitter_statuses(userID, number_of_tweets=10):
    statuses = []
    try:
        for status in tweepy.Cursor(api.user_timeline, screen_name=userID).items(number_of_tweets):
            serializer = StatusSerializer(data=status._json)
            statuses.append(serializer)
    except TweepError:
        pass #TODO setup an error log database, no process interrupting
    return statuses