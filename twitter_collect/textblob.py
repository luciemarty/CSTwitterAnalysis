from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")

wiki.tags

wiki.noun_phrases

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")

testimonial.sentiment

testimonial.sentiment.polarity

zen = TextBlob("Beautiful is better than ugly. "
...                "Explicit is better than implicit. "
...                "Simple is better than complex.")

for sentence in zen.sentences:
    print(sentence.sentiment)

from textblob import Word
    from textblob.wordnet import VERB
    word = Word("octopus")
    word.synsets
