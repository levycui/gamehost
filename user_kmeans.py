#!/usr/bin/python
# -*- coding:UTF-8 -*-
#Use k-means to classify, 4 class

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import operator

df = pd.read_table('user_count_num.txt', header=None, sep=',')
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