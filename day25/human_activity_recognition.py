# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 09:15:43 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
train_data=pd.read_csv("train.csv")
test_data=pd.read_csv("test.csv")

features_train=train_data.iloc[:,:-1].values
labels_train=train_data.iloc[:,-1].values
features_test=test_data.iloc[:,:-1].values
labels_test=test_data.iloc[:,-1].values


#logistic regression

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)
#predicting class labels
labels_pred=classifier.predict_proba(features_test)
#confusion matrix


print("score:",classifier.score(features_test,labels_test))


#using KNN
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=4 , p=2)
knn.fit(features_train,labels_train)
#Calculate Class Probabilities
probability1 = knn.predict_proba(features_test)

# Predicting the class labels
labels_pred1 = knn.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred1)
print(cm)
#score for knn
print("score:",knn.score(features_test,labels_test))


#using decision tree

from sklearn.tree import DecisionTreeClassifier
classifier2=DecisionTreeClassifier()
classifier2.fit(features_train,labels_train)

labels_pred=classifier2.predict(features_test)
from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred)) 

print("score:",classifier2.score(features_test,labels_test))




from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))



# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_train = labelencoder.fit_transform(labels_train)


# Building the optimal model using Backward Elimination
import statsmodels.api as sm
#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)

#adds a constant column to input data set.

features_opt = features_train[:,:]
regressor_OLS = sm.OLS(endog = labels_train, exog =features_opt).fit()
regressor_OLS.summary()

y=pd.DataFrame(labels_train)
x=pd.DataFrame(features_train)
cols=list(x.columns)
p=1
while(len(cols)>0):
    p=[]
    x_1=x[cols]
    x_1=sm.add_constant(x_1)
    model=sm.OLS(y,x_1).fit()
    p=pd.Series(model.pvalues.values[1:],index=cols)
    pmax=max(p)
    feature_with_pmax=p.idxmax()
    if(pmax>0.05):
        cols.remove(feature_with_pmax)
    else:
        break
selected_features=cols
print(selected_features)
features=features_train[:,selected_features]





