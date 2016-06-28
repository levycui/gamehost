#!/usr/bin/python
# -*- coding:UTF-8 -*-

import re

item10 = ''

#with open('datafile_buy_clean.txt','r') as df:
with open('datafile_sell_clean.txt','r') as df:

    for line in df.readlines():
        # print line
        (item1,item2,item3,item4,item5,item6,item7,item8,item9) = re.split('\|\|',line.strip())
        if item2=='PS3':
            item10 = '索尼电玩'
        if item2=='PS4':
            item10 = '索尼电玩'
        if item2=='PC':
            item10 = '其他'
        if item2=='WIIU':
            item10 = '任天堂'
        if item2=='3DS':
            item10 = '任天堂'
        if item2=='PSV':
            item10 = '索尼电玩'
        if item2=='XBox360':
            item10 = '微软电玩'
        if item2=='PSP':
            item10 = '索尼电玩'
        if item2=='NDS':
            item10 = '任天堂'
        if item2=='其他':
            item10 = '其他'
        if item2=='XBoxOne':
            item10 = '微软电玩'
        if item2=='WII':
            item10 = '任天堂'

        datanew =  '%s||%s||%s||%s||%s||%s||%s||%s||%s||%s\n' %(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)
        # print datanew
        #dataf = open("datafile_buy_tag.txt","a")
        dataf = open("datafile_sell_tag.txt","a")
        dataf.write(datanew)
        dataf.close()

    df.close()
