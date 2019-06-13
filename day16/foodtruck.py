# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:42:59 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
dataset=pd.read_csv('Foodtruck.csv')
#Check if any NaN values in dataset
dataset.isnull().any(axis=0)

dataset.plot(x='Population', y='Profit', style='o')  
plt.title('population vs Profit')  
plt.xlabel('population')  
plt.ylabel('Profit')  
plt.show()


features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 
val = np.array([3.073]).reshape(1,-1)
print ("estimated profit of jaipur:",regressor.predict(val))
