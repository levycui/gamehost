#!/usr/bin/python
# -*- coding:UTF-8 -*-

import pandas as pd
df = open("user_count.txt","r")
for line in df.readlines():
    line = line.split(',')
    datanew = str('1,' + line[1],)
    dataf = open("user_count_num.txt","a")
    dataf.write(datanew)
    dataf.close()
df.close()