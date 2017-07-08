#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import urllib
import urllib2
import json
from bs4 import BeautifulSoup

from lxml import etree

# 获取 lxml 对象，解析 html
def getpath(html):
    return etree.HTML(html)

# 获取豆瓣电影 tag 的 url

url = "https://movie.douban.com/j/search_tags?type=movie&source="



# 定义获取 ditc 格式的url解析

def get_result(url):

    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    result = json.loads(response.read())

    return result

def get_response(url):
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
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

'''

for n in xrange(0, len(movies)):
    item = movies[n]
    resp = get_response(item["url"])

    html = BeautifulSoup(resp, "lxml")

    title = html.select("h1")[0]

    title = title.select("span")[0]

    title = title.get_text()

    print title
    
'''

for n in xrange(0, len(movies)):
    itemx = movies[n]

    # respx = get_response(itemx["url"])

    # print type(respx)

    htmlx = getpath(itemx["url"])


    print type(htmlx)

    S0 = htmlx.xpath('/html/head/title/text()')



    S1 = htmlx.xpath('//span[@property="v:itemreviewed"]/text()')

    S2 = htmlx.xpath('//span[@class ="year"]/text()')

    S3 = htmlx.xpath('//span[@class ="pl"]/text()')

    S4 = htmlx.xpath('//comment()')



    print S1,S2,S3,S0,S4

    break




