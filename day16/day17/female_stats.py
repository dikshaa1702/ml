# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:46:31 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("female_stats.csv")
features=df.iloc[:,[1,2]].values
labels=df.iloc[:,0].values
feature1=df.iloc[:,1].values
feature2=df.iloc[:,2].values


import statsmodels.api as sm
#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)
features=sm.add_constant(features)
features_opt = features[:, [0,1,2]]

regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
print("both the factors including mom,s height and dad,s height is important")
#from the summary table all the column value of p is 0 which represent that the prob that column is not imp
print("When Father’s Height Is Held Constant, The Average Student Height Increases By 0.3035 Inches For Each One-Inch Increase In Mother’s Height")
print("When mother’s Height Is Held Constant, The Average Student Height Increases By 0.3879 Inches For Each One-Inch Increase In father’s Height.")
