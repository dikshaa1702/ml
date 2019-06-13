# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:50:09 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
auto=pd.read_csv("Automobile.csv")

#finding mean and replacing nan values
temp=auto['price'].mean()
auto['price']=auto['price'].fillna(temp)

#converting to np array
array=np.array(auto['price'])
print("converted to nparray:",array)
print("min price is:",auto['price'].min())
print("max price is:",auto['price'].max())
print("average price is:",auto['price'].mean())
print("standard deviation is:",np.std(auto['price']))