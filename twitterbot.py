#!/usr/bin/python3

import os
import random
import logging
import tweepy
from twitter_secrets import Secrets
from src.generate_unconditional_samples import sample_model

logfilename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bot.log')
logging.basicConfig(level=logging.DEBUG, filename=logfilename, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
logger.info(f'log file path: {logfilename}')

results = sample_model()
logger.info('Sampling model succeeds')

results = results.split('\n')[1:-1]
logger.info(f'Fetched {len(results)} samples')

results = [line for line in results if len(line) <= 140]

auth = tweepy.OAuthHandler(Secrets.CONSUMER_KEY, Secrets.CONSUMER_KEY_SECRET)
auth.set_access_token(Secrets.ACCESS_TOKEN, Secrets.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

api.update_status(random.choice(results))
