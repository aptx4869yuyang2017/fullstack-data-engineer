#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import urllib
import urllib2
import json
from bs4 import BeautifulSoup

# 获取豆瓣电影 tag 的 url

url = "https://movie.douban.com/j/search_tags?type=movie&source="



# 定义获取 ditc 格式的url解析

def get_result(url):

    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout=20)
    result = json.loads(response.read())

    return result

def get_response(url):
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request, timeout=20)
    return response





tags = get_result(url)

# dict 格式的 value 是 tag

tags = tags["tags"]

movies = []

for tag in tags:
    limits = 0
    while 1:

        # 拼接获取各个 tag 下的电影 list 的 url

        url_mlist = "https://movie.douban.com/j/search_subjects?type=movie&tag=" + tag + \
              "&page_limit=20&page_start=" + str(limits)

        result_mditc = get_result(url_mlist)
        # 获取 "subjects" 键下的值，是电影列表
        mdict = result_mditc["subjects"]


        if mdict == []:
            break

        limits += 20
        for item in mdict:
            movies.append(item)

        ##
        break

    ##
    break


for n in xrange(0, len(movies)):
    item = movies[n]
    resp = get_response(item["url"])

    html = BeautifulSoup(resp, "lxml")

    title = html.select("h1")[0]

    title = title.select("span")[0]

    title = title.get_text()

    print title












