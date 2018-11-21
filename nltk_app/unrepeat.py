import nltk

# 文本去重

word_data = "The Sky is blue also the ocean is blue also Rainbow has a blue colour."
nltk_tokens = nltk.word_tokenize(word_data)

unordered_tokens = set()
ordered_tokens = []
for word in nltk_tokens:
    if word not in unordered_tokens:
        unordered_tokens.add(word)
        ordered_tokens.append(word)

print(unordered_tokens)
print(ordered_tokens)
