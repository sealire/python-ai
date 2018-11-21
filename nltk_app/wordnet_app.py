from nltk.corpus import wordnet as wn

res = wn.synset('locomotive.n.01').lemma_names()
print(res)

resdef = wn.synset('ocean.n.01').definition()
print(resdef)

res_exm = wn.synset('good.n.01').examples()
print(res_exm)

res_a = wn.lemma('horizontal.a.01.horizontal').antonyms()
print(res_a)