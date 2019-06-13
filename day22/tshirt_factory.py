# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:25:21 2019

@author: DiPu
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("tshirts.csv")
features=data.iloc[:,[1,2]].values
plt.scatter(features[:,0],features[:,1])
plt.plot()
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],c="red",label="cluster1")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],c="blue",label="cluster2")
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],c="green",label="cluster3")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],c="yellow",label="centroid")