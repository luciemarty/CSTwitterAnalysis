from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")

print(wiki.sentiment.polarity)

for sentence in wiki.sentences :
    print(sentence.sentiment)

