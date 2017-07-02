#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='douban',\
                     port=8889, charset='utf8',\
                     cursorclass=MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

fr = open('douban_movie_clean.txt','r')

count = 0
for line in fr:
    count += 1
    print count
    if count == 1:
        continue

    line = line.strip().split("^")

    # Creat

    # cursor.execute(
    #     "insert into movie(title, url, rate, length, description) \
    #      values(%s, %s, %s, %s, %s)",
    #     [line[1], line[2], line[4], line[-3], line[-1], ]
    # )

cursor.close()
db.close