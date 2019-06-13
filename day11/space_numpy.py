# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:35:23 2019

@author: DiPu
"""
import numpy as np
# taking input 9 space separated digits
numbers=[int(n) for n in input("enter 9 numbers:").split()]
#converting into numpy array
x=np.array(numbers)
#reshaping to 2 d array
x=x.reshape(3,3)
print(x)