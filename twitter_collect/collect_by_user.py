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

"""On construit ensuite une liste, avec chaque élément une sous-liste avec le nom de la personne qui tweet, le contenu
du tweet, le nombre de retweet et le nombre de like"""
def collect_by_user(user_id,count):
    connexion =twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = int(count))
    collected=[]
    for tweet in statuses:
        collected=collected+[[tweet.user.name,tweet.text,tweet.retweet_count,tweet.favorite_count,tweet.created_at]]
    return collected

