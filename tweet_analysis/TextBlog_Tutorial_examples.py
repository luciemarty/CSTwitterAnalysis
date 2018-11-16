import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')
#nltk.download('wordnet')

from textblob import TextBlob
wiki = TextBlob("Python is a high-level, general-purpose programming language.")

print(wiki.tags)
print(wiki.noun_phrases)


testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print(testimonial.sentiment)
print(testimonial.sentiment.polarity)

zen = TextBlob("Beautiful is better than ugly. "
               "Explicit is better than implicit. "
               "Simple is better than complex.")
print(zen.words)
print(zen.sentences)


sentence = TextBlob('Use 4 spaces per indentation level.')
print(sentence.words)
print(sentence.words[2].singularize())
print(sentence.words[-1].pluralize())

#w = Word("went")
#print(w.lemmatize("v"))

from textblob import Word

word = Word("octopus")
print(Word("photo").definitions)

from textblob.wordnet import Synset
octopus = Synset('octopus.n.02')
shrimp = Synset('shrimp.n.03')
print(octopus,shrimp)
print(octopus.path_similarity(shrimp))

b = TextBlob("I havv goood speling!")
print(b.correct())

#w = Word('havv')
#print(w.spellcheck())

monty = TextBlob("We are no longer the Knights who say Ni. "
                    "We are now the Knights who say Ekki ekki ekki PTANG.")
print(monty.word_counts['ekki'])
print(monty.words.count('ekki'))
print(monty.words.count('ekki', case_sensitive=True)) #Case_sensitive-->Sensible aux majuscules/minuscules


en_blob = TextBlob(u'The sooner, the better')
print(en_blob.translate(to='fr'))


b = TextBlob(u"今年の夏の間に日本に行きました")
print(b.translate(from_lang='ja',to='fr'))

c = TextBlob("And now for something completely different.")
print(c.parse())

blob = TextBlob("Now is better than never.")
blob.ngrams(n=3)

for s in zen.sentences:
    print(s)
    print("---- Starts at index {}, Ends at index {}".format(s.start, s.end))

