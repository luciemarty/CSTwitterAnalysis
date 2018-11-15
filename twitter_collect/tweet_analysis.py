from twitter_collect.collect_candidate_actuality_tweets import *

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

print(max_rt('n'))


