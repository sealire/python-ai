import nltk
from file_read_backwards import FileReadBackwards

with FileReadBackwards("mgi.txt", encoding="utf-8") as BigFile:
    # getting lines by lines starting from the last line up
    for line in BigFile:
        word_data = line
        print(word_data)

        nltk_tokens = nltk.word_tokenize(word_data)
        nltk_tokens.reverse()
        print(nltk_tokens)
