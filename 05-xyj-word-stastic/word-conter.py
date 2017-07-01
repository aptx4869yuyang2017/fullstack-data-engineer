#!/usr/bin/env python
# coding=utf-8

import sys
import json

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



fw = open("result.json", "w")
fw.write(json.dumps(times))
fw.close()



times = sorted(times.iteritems(), key=lambda d:d[1], reverse=True)


fw = open("result.csv", "w")

for item in times:

    fw.write(item[0] + "," + str(item[1]) + "\n")


fw.close()

fr.close()

print len(word)
print len(times)