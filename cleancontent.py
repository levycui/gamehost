#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os
import sys
import re


# datafile buy clean
# with open('datafile_buy.txt','r') as df:
#     for line in df.readlines():
#         # print line
#         linenum = line.count('||')
#         if linenum == 8:
#             print line
#             dataf = open("datafile_buy_clean.txt","a")
#             dataf.write(line)
#             dataf.close()
#     df.close()

# datafile sell clean
with open('datafile_sell.txt','r') as df:
    for line in df.readlines():
        # print line
        linenum = line.count('||')
        if linenum == 8:
            print line
            dataf = open("datafile_sell_clean.txt","a")
            dataf.write(line)
            dataf.close()
    df.close()