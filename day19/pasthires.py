# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:40:27 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("PastHires.csv")

features=data.iloc[:,0:6].values
labels=data.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 1] = labelencoder.fit_transform(features[:, 1])
features[:, 4] = labelencoder.fit_transform(features[:, 4])
features[:, 3] = labelencoder.fit_transform(features[:, 3])
features[:, 5] = labelencoder.fit_transform(features[:, 5])
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
print("confusion matrix:",confusion_matrix(labels_test, labels_pred))  

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  

#train the model
from sklearn.ensemble import RandomForestClassifier
classifier= RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)                                         
labels_pred = classifier.predict(features_test)  

#Evaluating the algorithm
#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("cm_rf:",confusion_matrix(labels_test,labels_pred))  
print("cr:",classification_report(labels_test,labels_pred))  
print("AS:",accuracy_score(labels_test, labels_pred))
Score_rf = classifier.score(features_test,labels_test)
print("Score_rf:",Score_rf)

x=[10,1,4,0,1,0]
y=[10,0,4,1,0,1]
x=np.array(x).reshape(1,-1)
y=np.array(x).reshape(1,-1)
print("Hired: ",classifier.predict(x))
print("Hired: ",classifier.predict(y))
