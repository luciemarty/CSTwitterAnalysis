import tweepy
# We import our access keys:
from credentials import *
from tweepy.streaming import StreamListener


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


#Id_Place given by http://woeid.rosselliot.co.nz/
connection=twitter_setup()
trends1 = connection.trends_place(23424819) #Extract Twitter trends for France
data = trends1[0]
# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
trendsName = ','.join(names)
print(trendsName)
