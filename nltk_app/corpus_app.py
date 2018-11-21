from nltk.corpus import wordnet
from nltk.corpus import stopwords

print(stopwords.fileids())

stopwords.words('english')
print(stopwords.words()[620:640])

synonyms = []
for syn in wordnet.synsets("dog"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))

antonyms = []
for syn in wordnet.synsets("ahead"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())
print(set(antonyms))
