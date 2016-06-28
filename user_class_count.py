#!/usr/bin/python
# -*- coding:UTF-8 -*-
#The number of user_class Posting summary

import operator

df = open("user_class.txt")
count_dict = {}
for line in df.readlines():
    line = line.strip()
    count = count_dict.setdefault(line, 0)
    count += 1
    count_dict[line] = count
sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
for item in sorted_count_dict:
    datanew = "%s,%s" % (item[1],item[0] ) + '\n'
    dataf = open("user_class_count.txt","a")
    dataf.write(datanew)
    dataf.close()
df.close()