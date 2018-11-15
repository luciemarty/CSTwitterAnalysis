from twitter_collect.collect_candidate_actuality_tweets import *

def get_replies_to_candidate(num_candidate) :
    """cette fonction affiche sous format json tous les tweets reliés au candidat n """
    try :
        liste = get_candidate_queries('n')
        for search in liste:
            print(search)
            print(collect(str(search)))
    except IOError as error :
        print(error)

print(get_replies_to_candidate('n'))

