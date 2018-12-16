from pyltp import Segmentor
from pyltp import Postagger

seg = Segmentor()
seg.load("../ltp_model/cws.model")
words = seg.segment("你是那人间的四月天。")
print("| ".join(words))

split_word = ' '.join(words)
pos = Postagger()
pos.load("../ltp_model/pos.model")
postags = pos.postag(split_word)

for word, postag in zip(split_word, postags):
    print(word + '/' + postag, end=' ')
