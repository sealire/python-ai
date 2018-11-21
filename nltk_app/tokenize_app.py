import nltk

FileName = ("fgi.txt")

with open(FileName, 'r') as file:
    data = file.read()
    # print(data)

    nltk_tokens = nltk.word_tokenize(data)
    print(nltk_tokens)
    print("Number of Words: ", len(nltk_tokens))

    split_tokens = data.split()
    print(split_tokens)
    print("Number of Words: ", len(split_tokens))

sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print(nltk_tokens)

german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens = german_tokenizer.tokenize('Wie geht es Ihnen?  Gut, danke.')
print(german_tokens)

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print(nltk_tokens)
