# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:29:00 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("iq_size.csv")
labels=data.iloc[:,0].values
features=data.iloc[:,1:4].values


from sklearn.linear_model import LinearRegression
lin_reg1=LinearRegression()
lin_reg1.fit(features,labels)
value=np.array([90,70,150]).reshape(1,-1)
lin_reg1.predict(value)

import statsmodels.api as sm
features=sm.add_constant(features)
features_opt=features[:,[0,1,2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:, [0, 1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

from sklearn.linear_model import LinearRegression
#using column of ols summary
lin_reg=LinearRegression()
lin_reg.fit(features_opt,labels)
value=np.array([90]).reshape(1,-1)
lin_reg.predict(value)

#without using ols summary

