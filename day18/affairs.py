# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:01:09 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("affairs.csv")
features=data.iloc[:,0:8].values
labels=data.iloc[:,8].values

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [7])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]



from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.6, random_state = 40)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)


prob=classifier.predict_proba(features_test)


# Predicting the class labels
labels_pred = classifier.predict(features_test)

#creating confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("confusion matrix:",cm)

Score_lin = classifier.score(features_test, labels_test)
print(" score for linear regression:",Score_lin)

per_for_actual_affair=data['affair'].value_counts(normalize=True)[1]
print("percentage of women having actual affair",per_for_actual_affair)
data=np([]).reshape(1,-1)
labels_pred = classifier.predict(data)