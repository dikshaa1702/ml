# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:13:26 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
data=pd.read_csv("Bahubali2_vs_Dangal.csv")

features =data.iloc[:, 0].values
features=features.reshape(9,1)
labels = data.iloc[:,1:3 ].values 

"""
train the model now 
"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 
val = np.array([10]).reshape(1,-1)
temp=regressor.predict(val)
if temp[0,0]>temp[0,1]:
    print("Bahubali 2 will collect more")
else:
    print("Dangal will collect more")

