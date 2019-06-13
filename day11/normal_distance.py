# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:46:51 2019

@author: DiPu
"""

import numpy as np
import matplotlib.pyplot as plt
values=np.random.normal(150, 20, 1000)
plt.hist(values,bins=100) 
print("Standard Deviation is: ", np.std(values))
print("variance is: ", np.var(values))
