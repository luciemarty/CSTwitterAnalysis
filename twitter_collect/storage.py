import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from twitter_collect.twitter_connection_setup import *


def store_tweets(tweets,filename):
    # I open a file with writing access
    list_tweets = []
    with open(filename, 'w') as f:
        for tweet in tweets:
            # Every tweet is added to a list that will then be added to the Json file
            list_tweets.append(tweet._json)
        json.dump(list_tweets, f, indent=4)


def collect_to_pandas_dataframe(user_id):
    connexion = twitter_setup()
    tweets = connexion.user_timeline(id = user_id, count = 20)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

