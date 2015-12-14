#!/usr/bin/python
# -*- coding:utf-8 -*-

from pyspark import SparkConf, SparkContext
import os

os.environ["SPARK_HOME"] = "/opt/spark-hadoop"

# 将 TopKeyword 做一些 ML 的工作