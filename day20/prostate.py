# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:51:51 2019

@author: DiPu
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter=' ')
labels=data.iloc[:,-1].values
features=data.iloc[:,0:8].values
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.5,random_state=0)

#Train the unregularized model (linear regressor) and calculate the mean squared error
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(features_train,labels_train)


#Predict on test and training data

predict_test_lm =lm.predict(features_test )  
from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is:") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lm),2) )

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

lm_lasso=Lasso()
lm_ridge=Ridge()
lm_elastic=ElasticNet()

lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)


predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))



#predict whether lpsa is high or low, from other variables


df= pd.read_csv('http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat',delimiter=" ")
df["lpsa"] = data["lpsa"].map(lambda x: True if x>2.5 else False, range(1, 10))


#prepare the data to train the model
features = df.iloc[:,:-1].values  
labels = df.iloc[:, 8].values 
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print("cm:",cm)
Score = classifier.score(features_test,labels_test)
print("Score:",Score)

