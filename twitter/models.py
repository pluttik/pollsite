from django.db import models

class Tweet(models.Model):
    tweet_text = models.CharField(max_length=200)
    tweet_author = models.CharField(max_length=200)
    def __str__(self):
        return self.tweet_text
    def __author__(self):
        return self.tweet_author