# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:48:50 2019

@author: DiPu
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#loading dataset
from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
iris= pca.fit_transform(iris)
explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3,init="k-means++",random_state=0)
pred_cluster=kmeans.fit_predict(iris)

plt.scatter(iris[pred_cluster == 0, 0], iris[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(iris[pred_cluster == 1, 0], iris[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(iris[pred_cluster == 2, 0], iris[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()
