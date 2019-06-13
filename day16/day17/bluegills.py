# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:43:33 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("bluegills.csv")

features=data.iloc[:,0].values.reshape(-1,1)
labels=data.iloc[:,1].values

# Visualising the Linear Regression results
plt.scatter(features, labels)

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(features,labels)


plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('age')
plt.ylabel('height')
plt.show()

Score_lin = lin_reg.score(features, labels)
print(" score for linear regression:",Score_lin)
#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 10)
features_poly = poly_object.fit_transform(features)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)



plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Age')
plt.ylabel('height')
plt.show()
value=np.array([5]).reshape(1,-1)
print("length of a randomly selected five-year-old bluegill fish:",lin_reg_2.predict(poly_object.transform(value)))

score_quad = lin_reg_2.score(features_poly, labels)
print("score for polynomial regression",score_quad)