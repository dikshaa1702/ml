# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:44:12 2019

@author: DiPu
"""
from collections import Counter
import numpy as np
from scipy import stats
no=np.random.randint(5,15,40)
print(no)
#with numpy finding max occurance of no
print("Mode value is: ", stats.mode(no)[0])

#without numpy

li1=no.tolist()
count=Counter(li1)
dic=dict(count)
val=max(dic.values())
print(dic[val])
