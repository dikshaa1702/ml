# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:59:55 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("tree_addhealth.csv")

data['age'] = data['age'].fillna(data['age'].mean())

features=data.iloc[:,[0,1,2,3,4,5,6,8,9,10,11,12,13,14]].values

data['ESTEEM1'] = data['ESTEEM1'].fillna(data['ESTEEM1'].mean())
data['TREG1'] = data['TREG1'].fillna(0)
labels=data.iloc[:,-4].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.6, random_state = 40)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)


prob=classifier.predict_proba(features_test)
from sklearn.metrics import confusion_matrix

labels_pred = classifier.predict(features_test)

cm = confusion_matrix(labels_test, labels_pred)
print("confusion matrix:",cm)

data['EXPEL1'] = data['EXPEL1'].fillna(0)
labels=data