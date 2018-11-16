from twitter_collect.collect import *

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

#ID Trump 25073877
