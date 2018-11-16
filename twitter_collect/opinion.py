from twitter_collect.collect import *
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#ID Trump 25073877

def tweets_sentiment_analysis(name):
    """analyse des tweet mentionnant name
    retourne la polarité moyenne et la subjectivité moyenne sur l'ensemble des tweets collectés"""
    connexion=twitter_setup()
    tweets = connexion.search(name, count = 50)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    tweets_list = data['tweet_textual_content'].values
    polarity = []
    subjectivity = []
    for tweet in tweets_list:
        Analysis=TextBlob(tweet).sentiment
        polarity += [Analysis[0]]
        subjectivity += [Analysis[1]]
    print('For '+name+', we get :')
    print('Average polarity : ' + str(np.average(polarity)))
    print('Average subjectivity : '+ str(np.average(subjectivity)))

def percentage_pos_neg_tweets(name) :
    """cette fonction renvoie le poucentage de tweets positifs, négatifs et neutre qui contiennent name"""
    connexion = twitter_setup() # on crée des listes vides qui vont contenir les différents tweets en fonction de leur analyse par TextBlob
    pos_tweets = []
    neu_tweets = []
    neg_tweets = []
    tweets = connexion.search(name, count = 100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    tweets_list = data['tweet_textual_content'].values
    for tweet in tweets_list:
        analysis = TextBlob(tweet).sentiment
    # Si la polarité est >0 : le tweet est positif
        if analysis[0]>0:
            pos_tweets.append(tweet)
    # si la polarité est <0 : le tweet est négatif
        elif analysis[0]<0:
            neg_tweets.append(tweet)
    # sinon, le tweet est neutre
        else:
            neu_tweets.append(tweet)
    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))


def représentation_pol_subj(name) :
    """représente la polarité en fonction de la subjectivité des tweets mentionnant name"""
    connexion=twitter_setup()
    tweets = connexion.search(name, count = 50)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    tweets_list = data['tweet_textual_content'].values
    sns.set(style="white", color_codes=True)
    y = [TextBlob(tweet).sentiment[0] for tweet in tweets_list]
    x = [TextBlob(tweet).sentiment[1] for tweet in tweets_list]
    grid = sns.JointGrid(x, y, space=0, height=6, ratio=50)
    grid.plot_joint(plt.scatter, color="r")
    grid.plot_marginals(sns.rugplot, height=1, color="g")
    grid.set_axis_labels(xlabel = 'Subjectivity', ylabel='Polarity')
    plt.xlim(0,1)
    plt.ylim(-1,1)
    plt.show()



