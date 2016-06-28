#!/usr/bin/python
# -*- coding:UTF-8 -*-
#coding:utf-8

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import sys
import os
import re


def getPage(href):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(
        url = href ,
        headers = headers
    )
    try:
        post = urllib2.urlopen(req)
    except urllib2.HTTPError,e:
        print e.code
        print e.reason
    return post.read()

#url and page_num
url = 'http://www.youxiwugui.com/gameconsole/'
getPageNum = 114

def getEvery(url):
    hrefList = []
    page = BeautifulSoup(getPage(url))
    # print page
    div = page.find('div',id='listSell')
    # print div
    spanList = div.find_all('span',class_='tradetitle')
    # print spanList
    for li in spanList:
        href = 'http://www.youxiwugui.com' + li.a.get('href')
        if href!='http://www.youxiwugui.com/gameconsole/':
            # print href
            hrefList.append(href)
    return hrefList


#===============================================================================
# def getAll(href):
#     page=BeautifulSoup(getPage(href))
#     div = page.find('div',class_='list_3',id='experts')
#     for li in div.find_all('li'):
#         name = li.get_text()
#         href = li.a.get('href')
#         getBlog(name,href)

#===============================================================================

def getText(href):
    page = BeautifulSoup(getPage(href))

    df = open("datafile_sell.txt","a")

    #print num and hostclass and committime
    div_list = page.find('div',class_='cr_botfile')
    num = div_list.find('span',class_='cr_date')
    hostclass = div_list.find('font')
    committime = div_list.find('em')
    num=num.get_text()
    hostclass=hostclass.get_text()
    committime = committime.get_text()
    # print num+',',
    df.write(num+'||',)
    # print hostclass+',',
    df.write(hostclass+'||',)
    # print committime+',',
    df.write(committime+'||',)

    #print uid
    div_list = page.find('div',class_='rightside')
    result = div_list.find_all('div',class_='sd')
    for content in result:
        # print content
        resultspan = content.div.get_text().strip().split("\n")
        for contenttext in resultspan[1:2]:
            if contenttext.strip() =='':
                content
            else:
                # print contenttext.strip()+',',
                df.write(contenttext.strip()+'||',)

    #print title
    div_list = page.find('div',class_='cr_h1title')
    title = div_list.find('p')
    title=title.get_text()
    # print title+',',
    df.write(title+'||',)
    # print href+',',
    df.write(href+'||',)
    # print title+',',
    df.write(title+'||',)



    #print prices and address
    div_list = page.find('div',class_='rightside')
    # m = re.search("^# (.+)/.*$", a, re.M)
    result = div_list.find_all('div',class_='trade_info')
    for content in result:
        resultspan = content.ul.get_text().split("\n")
        for contenttext in resultspan:
            # print contenttext
            if u'所在地' in contenttext:
                # print contenttext[3:]+',',
                df.write(contenttext[3:]+'||',)
            if u'价格' in contenttext:
                # print contenttext[3:]+"\n"
                df.write(contenttext[3:].replace(',','')+"\n")
    df.close()


def getURL():
    i =1
    for i in range(1,(getPageNum+1)):
        url = 'http://www.youxiwugui.com/gameconsole/default.aspx?page=' + str(i)
        # print url
        href = getEvery(url)
        for con in href:
            # print con
            getText(con)
        i+=1
        # print '======================OK'

#===============================================================================

if __name__=="__main__":
    # hrefList = getEvery(url)
    reload(sys)
    sys.setdefaultencoding('utf-8')
    getURL = getURL()
    # for href in hrefList:
    #     getAll(href)
