# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:03:15 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("breast_cancer.csv")
df['G']=df['G'].fillna(df['G'].mean())
labels=df.iloc[:,-1].values
features=df.iloc[:,1:10].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.5,random_state=0)

from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)

print("confusion matrix:",cm)
print("score is:",classifier.score(features_test,labels_test))

data=[6,2,5,3,9,4,7,2,2]
data=np.array(data).reshape(1,-1)

temp=classifier.predict(data)[0]
if temp==4:
    print(" Malignant tumor")
else:
    print("Benign tumor ")