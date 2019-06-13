# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:24:31 2019

@author: DiPu
"""

s=map(int,input().split(','))
    
if all(items>=0 for items in s) and any( item == item[::-1] for item in s):
    print("true")
else:
    print("false")