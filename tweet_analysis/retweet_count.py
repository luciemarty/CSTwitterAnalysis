from twitter_collect.tweet_collect_whole import *
from twitter_collect.collect_by_user import *

"""On obtient les informations sur le tweet ayant recueilli le plus de RT"""
def max_retweet(Liste):
    Max_RT=0
    Max_tweet=[]
    for i in range(len(Liste)):
        if Liste[i][2]>=Max_RT:
            Max_tweet=Liste[i]
            Max_RT=Liste[i][2]
    return Max_tweet

# Exemple avec les tweets de M.Macron
#print(collect_by_user(1976143068,count=100))
#print (max_retweet(collect_by_user(1976143068,count=10)))

""" Exemple à l'aide de la fonction tweet_collect_whole (Mot-clés/hashtag)
print(get_candidate_queries(1, "CandidateData"))
print(max_retweet(get_candidate_queries(1, "CandidateData")))"""


"""On modélise le nombre de RT pour une liste de tweets, qui du fait de la méthode de récolte, sont classés du plus récent"""
import matplotlib.pyplot as plt
import numpy as np
def modelisation_RT(Liste):
    x=[]
    y=[]
    for i in range(-len(Liste),-1):
        x=x+[Liste[i][4]]
        y=y+[Liste[i][2]]
    plt.plot(x,y,color="red",marker="+",linewidth=0.2)
    plt.show()

"Modélisation des retweets aux tweets de D.Trump, pour les 200 derniers tweets"
#print(modelisation_RT(collect_by_user(25073877,count=200)))
"Modélisation des retweets aux tweets de B.Obama, pour les 200 derniers tweets"
print(modelisation_RT(collect_by_user(813286,count=200)))


