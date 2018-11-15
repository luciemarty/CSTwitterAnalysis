from twitter_collect.collect import *


def get_candidate_queries(num_candidate):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        file_hashtag_candidate= '/Users/marty/PycharmProjects/twitterPredictor/CandidateData/hashtag_candidate_'+str(num_candidate)+'.txt'
        file_keywords_candidate='/Users/marty/PycharmProjects/twitterPredictor/CandidateData/keywords_candidate_'+str(num_candidate)+'.txt'
        fichier_hashtag = open(file_hashtag_candidate, "r")
        fichier_keywords = open(file_keywords_candidate, "r")
        liste = []
        for line in fichier_hashtag.readlines():
            liste.append(str(line))
        for line in fichier_keywords.readlines():
            liste.append(str(line))
        return liste
    except IOError as error:
        print(error)

print(get_candidate_queries('n'))
