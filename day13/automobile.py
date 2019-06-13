# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:47:25 2019

@author: DiPu
"""

import pandas as pd
import matplotlib.pyplot as plt
dt=pd.read_csv("Automobile.csv")
series = dt["make"].value_counts()
explode = (0.5,0,0,0,0,0,0.5,0,0,0,0)

plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11], autopct='%2.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
