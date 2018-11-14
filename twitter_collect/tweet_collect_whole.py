
from twitter_collect.collect import *
from twitter_collect.collect_by_streaming import *
from twitter_collect.collect_by_user import *



"""Extrait les tweets à l'aide de la fonction collect à partir des hashtags et des mots-clés du candidat en question"""

def get_candidate_queries(num_candidate, file_path):
    try:
        file_hashtag_candidate='/Users/PaulJoly/PycharmProjects/twitterPredictor/'+str(file_path)+'/hashtag_'+str(num_candidate)+'.txt'
        file_keywords_candidate='/Users/PaulJoly/PycharmProjects/twitterPredictor/'+str(file_path)+'/keywords_candidate_'+str(num_candidate)+'.txt'
        fichier_hashtag = open(file_hashtag_candidate, "r")
        fichier_keywords = open(file_keywords_candidate, "r")
        for line in fichier_hashtag.readlines():
            print("")
            print(line)
            tweets=(collect(line))
            for tweet in tweets:
                print(tweet.text)
        for line in fichier_keywords.readlines():
            print("")
            print(line)
            tweets=(collect(line))
            for tweet in tweets:
                print(tweet.text)
    except IOError as error:
        print(error)

print (get_candidate_queries(1,'CandidateData'))


#for tweet in tweets:
    #    print(tweet.text)
