from twitter_collect.collect import *
from twitter_collect.collect_by_streaming import *
from twitter_collect.collect_by_user import *
import json

#Convert @Id to id_user with https://tweeterid.com/

#Exemples avec Macron et Blanquer
print(collect_by_user(1976143068,count=30))
print(collect_by_user(360019007,count=30))


