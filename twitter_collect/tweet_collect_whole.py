import tweepy
from twitter_collect.collect import *
from twitter_collect.collect_by_streaming import *
from twitter_collect.collect_by_user import *



"""Extrait les tweets à l'aide de la fonction collect à partir des hashtags et des mots-clés du candidat en question
On construit ensuite une liste, avec chaque élément une sous-liste avec le nom de la personne qui tweet, le contenu
du tweet, le nombre de retweet et le nombre de like"""

def get_candidate_queries(num_candidate, file_path):
    try:
        file_hashtag_candidate='/Users/PaulJoly/PycharmProjects/twitterPredictor/'+str(file_path)+'/hashtag_'+str(num_candidate)+'.txt'
        file_keywords_candidate='/Users/PaulJoly/PycharmProjects/twitterPredictor/'+str(file_path)+'/keywords_candidate_'+str(num_candidate)+'.txt'
        fichier_hashtag = open(file_hashtag_candidate, "r")
        fichier_keywords = open(file_keywords_candidate, "r")
        collected=[]
        for line in fichier_hashtag.readlines():
            #print("")
            #print(line)
            tweets=(collect(line))
            for tweet in tweets:
                #print(tweet.text)
                collected=collected+[[tweet.user.name,tweet.text,tweet.retweet_count,tweet.favorite_count]]
        for line in fichier_keywords.readlines():
            #print("")
            #print(line)
            tweets=(collect(line))
            for tweet in tweets:
                #print(tweet.text)
                collected=collected+[[tweet.user.name,tweet.text,tweet.retweet_count,tweet.favorite_count]]
        return collected
    except IOError as error:
        print(error)


