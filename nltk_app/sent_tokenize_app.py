import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

text = nltk.word_tokenize("A Python is a serpent which eats eggs from the nest")
tagged_text = nltk.pos_tag(text)
print(tagged_text)

nltk.help.upenn_tagset('NN')
nltk.help.upenn_tagset('IN')
nltk.help.upenn_tagset('DT')
nltk.help.upenn_tagset('JJ')

sample = gutenberg.raw("blake-poems.txt")
tokenized = sent_tokenize(sample)
for i in tokenized[:2]:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)
    print(tagged)
