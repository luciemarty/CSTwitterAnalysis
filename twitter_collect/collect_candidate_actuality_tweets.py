from twitter_collect.collect import *
from twitter_collect.collect_by_streaming import *
from twitter_collect.collect_by_user import *
import json

#Convert @Id to id_user with https://tweeterid.com/

#Exemples avec Macron et Mélenchon
print(collect_by_user(1976143068,count=5))
#print(collect_by_user(80820758,count=20))


