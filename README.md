## TopKeyword
Extract hot keywords of questions on Zhihu and make some use of these words.

## 依赖
+ Jieba 分词
+ Python 版本 Spark

## 步骤

```
MySQL 数据库 question 表导出为 question.txt ——> 使用 Jieba 分词 ——> 存储分词结果 ——> Spark 进行词频统计 ——> 排序选出 Top 10 ——> 做一些 ML 的预测
```

## 目录结构

```
└── TopKeyword
    ├── question_title.txt # 知乎抓取的近期时间内的标题
    ├── question.txt       
    ├── question_word.txt  # 将标题进行分词
    ├── README.md
    ├── wordcount.py       # 分词，词频统计主逻辑
    ├── machinelearning.py # 把结果做一些 ML 的工作
    └── wordcount_result   # Spark 词频统计结果
        ├── part-00000
        └── _SUCCESS
```
