"""On utilise ici des tweets extraits grâce aux user_id"""


import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')
#nltk.download('wordnet')

from textblob import TextBlob
from twitter_collect.collect import *
from twitter_collect.collect_by_streaming import *
from twitter_collect.collect_by_user import *
"""Application aux tweets de B.Obama"""
List=(collect_by_user(813286,count=200))
print(List)
def Tweet_poll(List):
    Polarity=[]
    Count_Positive=0
    Count_Negative=0
    Count_Neutral=0
    for i in range(len(List)):
        tweet_text=TextBlob(List[i][1])
        print(tweet_text)
        polarity_for_this_tweet=tweet_text.sentiment.polarity
        Polarity=Polarity+[polarity_for_this_tweet]
        if polarity_for_this_tweet<(-0.3):
            Count_Negative=Count_Negative+1
        elif polarity_for_this_tweet>(0.3):
            Count_Positive=Count_Positive+1
        else:
            Count_Neutral=Count_Neutral+1
        Total_tweet=len(Polarity)
    print([Polarity])
    return([Count_Positive/Total_tweet,Count_Neutral/Total_tweet,Count_Negative/Total_tweet])

Info=[Tweet_poll(collect_by_user(813286,count=200)),Tweet_poll(collect_by_user(25073877,count=200)),Tweet_poll(collect_by_user(747807250819981312,count=200)),Tweet_poll(collect_by_user(14260960,count=200))]
print(Info)
import matplotlib.pyplot as plt

Name=["Obama","Trump","May","Trudeau"]
X=[]
Y=[]
Z=[]
for i in range(0,4):
    X=X+[Info[i][0]]
    Y=Y+[Info[i][1]]
    Z=Z+[Info[i][2]]
print(X,Y,Z)
plt.plot(Name,X)
plt.plot(Name,Y)
plt.plot(Name,Z)
plt.title("Positive:blue,Neutral:Orange,Negative:Green")
plt.show()
