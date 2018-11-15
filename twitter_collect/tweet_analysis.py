from twitter_collect.collect_candidate_actuality_tweets import *
from twitter_collect.collect import *

def max_rt(num_candidate) :
    """fonction qui à partir des fichier hashtag_candidate_n.txt et keywords_candidate_n.txt renvoie le tweet avec le plus de RT"""
    try :
        liste = get_candidate_queries('n')
        res = ''
        a = 0
        for search in liste:
            connexion = twitter_setup()
            tweets = connexion.search(str(search),language="french",rpp=100)
            for tweet in tweets:
                if float(tweet.retweet_count) > a :
                    a = float(tweet.retweet_count)
                    res = tweet.text
        print ('Le tweet avec la plus de RT est le tweet :', res, ' avec ', a, ' RT' )
    except IOError as error :
        print(error)


def visualisation(id_num) :
    """affiche la représentation du nombre de RT en fonction de la date concernant le candidat id_num"""
    try :
        connexion = twitter_setup()
        statuses = connexion.user_timeline(id = user_id, count = 200)
        date = []
        nb_RT =[]
        for status in statuses:
            date.append(float(status.retweet_count))
            nb_RT.append(status.created_at)
    




