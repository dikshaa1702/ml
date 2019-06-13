# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:50:30 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets 
iris = datasets.load_iris()
features=pd.DataFrame(iris.data,columns=iris.feature_names)
labels=iris.target

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("cm:",cm)


print("Score:",classifier.score(features_test,labels_test))