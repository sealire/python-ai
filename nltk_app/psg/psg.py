import jieba.posseg as psg


def pross(text):
    psg_list = psg.cut(text)
    print(" ".join(['{0}/{1}'.format(w, t) for w, t in psg_list]))


if __name__ == '__main__':
    pross("词汇不足也一直是中国考生的通病")
    pross("你是那人间的四月天")
