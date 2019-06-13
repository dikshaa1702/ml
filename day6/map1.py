# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:53:49 2019

@author: DiPu
"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
g=list(map(lambda x:random.choice(code_names),names))
print(g)