#!/usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

fr = open("xyj.txt", "r")

word = []
times = {}

for line in fr:
    line = line.strip()

    if len(line) == 0:
        continue

    line = unicode(line)

    for x in xrange(0, len(line)):

        if not line[x] in word:
            word.append(line[x])

        if not times.has_key(line[x]):
            times[line[x]] = 0

        times[line[x]] += 1

print len(word)
print len(times)


print "hello"
