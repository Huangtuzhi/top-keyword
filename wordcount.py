#!/usr/bin/python
# -*- coding:utf-8 -*-

from pyspark import SparkConf, SparkContext
import os
import sys
import jieba

reload(sys)
sys.setdefaultencoding("utf-8")

os.environ["SPARK_HOME"] = "/opt/spark-hadoop"


def divide_word():
    word_txt = open('question_word.txt', 'a')

    with open('question_title.txt', 'r') as question_txt:
        question = question_txt.readline()
        while(question):
            seg_list = jieba.cut(question, cut_all=False)
            line = " ".join(seg_list)
            word_txt.write(line)
            question = question_txt.readline()
    question_txt.close()
    word_txt.close()


def word_count():
    sc = SparkContext("local", "WordCount")
    text_file = sc.textFile("./question_word.txt").cache()
    counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile("./wordcount_result")


def parse_data_get_topK():
    text = open('./wordcount_result/part-00000', 'r')
    word_count_str = text.readline()

    queue_dict = {}
    while(word_count_str):
        str_list = list(word_count_str)
        # 去掉括号
        str_list.pop(0)
        str_list.pop(len(str_list)-2)
        word_count_str = "".join(str_list)

        word = word_count_str.split(', ')[0]
        count = word_count_str.split(', ')[1]

        # 添加到字典中
        queue_dict[word] = count
        word_count_str = text.readline()
    text.close()
    sorted_list = sorted(queue_dict.iteritems(), key=lambda d:d[1], reverse = True)

    loop = 0
    top_queue = {}
    for one in sorted_list:
        top_queue[str(one[0])] = str(one[1])

        # 返回 topK KeyWords
        # print one[0].decode('unicode-escape'), one[1]
        loop += 1
        if (loop == 50):
            break
    return top_queue


if __name__ == "__main__":
    # 结巴分词
    # divide_word()

    # Spark 词频计数
    # word_count()

    # 词频排序
    dict = parse_data_get_topK()
    sorted_list = sorted(dict.iteritems(), key=lambda d:d[1], reverse = True)
    for one in sorted_list:
        print one[0].decode('unicode-escape'), one[1]