# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:21:01 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_fwf("Auto_mpg.txt")
data.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
data["horsepower"]=data["horsepower"].replace('?','0')
labels=data.iloc[:,0].values
features=data.iloc[:,1:8].values

#Display the Car Name with highest miles per gallon value
max_glp=data.loc[data['mpg'].idxmax()]
print("Car Name with highest miles per gallon value",max_glp[-1])


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.6, random_state=0) 

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  


from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
from sklearn.metrics import confusion_matrix

Score_dt = regressor.score(features_test,labels_test)
print("Score_df:",Score_dt)


#using forest 
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  

#Evaluating the algorithm
from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred)))  


x=[6,215,100,2630,22.2,80,3]
x=np.array(x).reshape(1,-1)
print("mpg_rf: ",regressor.predict(x))
