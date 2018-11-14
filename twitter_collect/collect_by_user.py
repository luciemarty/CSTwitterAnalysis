import tweepy
from credentials import *


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


def collect_by_user(user_id):
    connexion =twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 10)
    for status in statuses:
        print(status.text)
    return statuses

print(collect_by_user(80820758))
