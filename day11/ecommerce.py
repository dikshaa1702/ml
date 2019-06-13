# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:20:51 2019

@author: DiPu
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
incomes.sort()
print (incomes)
#creating histogram
plt.hist(incomes,bins=50) 
plt.xlabel('incomes')
plt.ylabel('persons')

#finding mean and median using numpy
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
incomes = np.append(incomes, [10000])


