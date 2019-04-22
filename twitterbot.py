#!/usr/bin/python3

import random
import tweepy
from twitter_secrets import Secrets
from src.generate_unconditional_samples import sample_model


results = sample_model()
results = results.split('\n')[1:-1]
results = [line for line in results if len(line) <= 140]

auth = tweepy.OAuthHandler(Secrets.CONSUMER_KEY, Secrets.CONSUMER_KEY_SECRET)
auth.set_access_token(Secrets.ACCESS_TOKEN, Secrets.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status(random.choice(results))
