# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:15:01 2019

@author: DiPu
"""

li=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
l=tuple(x.strip() for x in input().split(','))
s1=set(l)
s2=set(li)
print(s1.union(s2))