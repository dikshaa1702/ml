# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:19:06 2019

@author: DiPu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('crime_data.csv')
features = dataset.iloc[:, [1,2,4]].values


from sklearn.decomposition import PCA
pca=PCA(n_components=2)
features_df=pca.fit_transform(features)
explained_variance=pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
pred_cluster=kmeans.fit_predict(features)

plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],c='blue',label='cluster1')
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],c='red',label='cluster2')
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],c='green',label='cluster3')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],c='gold',label='centroid')