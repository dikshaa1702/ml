# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:51:05 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("mushrooms.csv")
labels=data.iloc[:,0].values
features=data.iloc[:,[5,21,22]].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels= labelencoder.fit_transform(labels)


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:,0])
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,2] = labelencoder.fit_transform(features[:,2])



from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [8])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [13])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]



from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.6, random_state = 40)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("confusion matrix:",cm)

Score_lin = classifier.score(features_test, labels_test)
print(" score for linear regression:",Score_lin)
