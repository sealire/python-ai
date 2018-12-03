# coding=utf-8

# 分词
import jieba

# PCFG句法分析
from nltk.parse import stanford
import os

if __name__ == '__main__':

    string = '你是那人间的四月天。'
    seg_list = jieba.cut(string, cut_all=False, HMM=True)
    seg_str = ' '.join(seg_list)

    print(seg_str)
    root = 'stanford/'
    parser_path = root + 'stanford-parser.jar'
    model_path = root + 'stanford-parser-3.9.2-models.jar'

    # 指定JDK路径
    if not os.environ.get('JAVA_HOME'):
        JAVA_HOME = '/usr/lib/jvm/jdk1.8'
        os.environ['JAVA_HOME'] = JAVA_HOME

    # PCFG模型路径
    pcfg_path = 'stanford/chinesePCFG.ser.gz'

    parser = stanford.StanfordParser(
        path_to_jar=parser_path,
        path_to_models_jar=model_path,
        model_path=pcfg_path
    )

    sentence = parser.raw_parse(seg_str)
    for line in sentence:
        print(line.leaves())
        line.draw()
