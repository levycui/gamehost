#!/usr/bin/python
# -*- coding:UTF-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import operator

#索尼电玩
#任天堂
#微软电玩

# the first progress
#18,游戏发烧友	索尼电玩
#14,罗格玫兰	索尼电玩

df = open('user_class_count.txt')

for line in df.readlines():
    # print line
    if "微软电玩" in line:
        # print line,
        # dataf = open("user_class_count_sony.txt","a")
        # dataf = open("user_class_count_Nintendo.txt","a")
        dataf = open("user_class_count_micosoft.txt","a")
        dataf.write(line)
        dataf.close()
df.close()


# the second progress
#1,18
#1,14

# df = open('user_class_count_micosoft.txt')
# for line in df.readlines():
#     line = line.split(',')
#     datanew = str('1,' + line[0] +'\n')
#     # dataf = open("user_class_count_sony_num.txt","a")
#     #dataf = open("user_class_count_Nintendo_num.txt","a")
#     dataf = open("user_class_count_micosoft_num.txt","a")
#     dataf.write(datanew)
#     dataf.close()
# df.close()

# the third progress

# df = pd.read_table('user_class_count_sony_num.txt', header=None, sep=',')
# df = pd.read_table('user_class_count_Nintendo_num.txt', header=None, sep=',')
df = pd.read_table('user_class_count_micosoft_num.txt', header=None, sep=',')
# print df.loc[:10].values
# df1, classes = make_blobs(100, centers=4)

# print df.loc[:,0].values
k_means = KMeans(n_clusters=4,random_state=0)
print k_means.fit(df)
print k_means.cluster_centers_
datanum = k_means.labels_
# print datanum

#count class number
count_num = {}
for line in datanum:
    count = count_num.setdefault(line, 0)
    count += 1
    count_num[line] = count
sorted_count_dict = sorted(count_num.iteritems(), key=operator.itemgetter(1), reverse=True)
for item in sorted_count_dict:
    datanew = "%s,%d" % (item[0], item[1])
    print datanew

f, ax = plt.subplots(figsize=(7.5, 7.5))
# rgb = np.array(['r', 'g', 'b', 'y'])
ax.scatter(df.loc[:,0].values, df.loc[:,1].values,color=['r', 'g', 'b', 'y'])
ax.scatter(k_means.cluster_centers_[:, 0],k_means.cluster_centers_[:, 1], marker='*', s=200,color='red', label='Centers')

ax.set_title("k_means")
ax.legend(loc='best')
# plt.show()