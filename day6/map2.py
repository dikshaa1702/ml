# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:10:30 2019

@author: DiPu
"""

names = ['Mary', 'Isla', 'Sam']
g=list(map(lambda x:hash(x) ,names))
print(g)