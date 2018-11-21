from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

fields = gutenberg.fileids()
print(fields)

sample = gutenberg.raw("blake-poems.txt")
token = sent_tokenize(sample)
for para in range(2):
    print(token[para])
