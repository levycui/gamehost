#!/usr/bin/python
# -*- coding:UTF-8 -*-
#The number of users Posting summary

import operator

df = open("user.txt")
count_dict = {}
for line in df.readlines():
    line = line.strip()
    count = count_dict.setdefault(line, 0)
    count += 1
    count_dict[line] = count
sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
for item in sorted_count_dict:
    datanew = "%s,%d" % (item[0], item[1]) + '\n'
    dataf = open("user_count.txt","a")
    dataf.write(datanew)
    dataf.close()
df.close()