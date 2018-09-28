from django.shortcuts import render
from django.http import HttpResponse
#from django.views import generic
import tweepy, os

from .models import Tweet

consumer_key = os.environ["POLLSITE_TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["POLLSITE_TWITTER_CONSUMER_SECRET"]
access_token = os.environ["POLLSITE_TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["POLLSITE_TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweet_list = []
    
statuses = api.search('#django', count=10)
for status in statuses:
    tweet_list.append(status.user.name + ': ' + status.text)
    
print(tweet_list)
    
def index(request):
    context = {'tweet_list': tweet_list}
    return render(request, 'twitter/index.html', context)