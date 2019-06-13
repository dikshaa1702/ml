# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:22:01 2019

@author: DiPu
"""
from functools import reduce
people =[{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
b=(list(filter(lambda x: True if 'height' in x else False,people)))
g=list(map(lambda x:x['height'],b ))
c=len((list(filter(lambda x: True if 'height' in x else False,people))))
d=reduce(lambda x,y:x+y,g)
print("average height:",d/c)