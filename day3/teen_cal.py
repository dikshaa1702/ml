# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:40:03 2019

@author: DiPu
"""
#import ast
#print("enter key and value")
#while True:
def fix_teen(item):
    li=[13,14,15,16,17,18,19]
    if item==15 and item==16:
        return item
    else:
        return 0
from ast import literal_eval
inp=input("enter dictionary")
sample=literal_eval(inp)
print(sample)
sum=0
for value in sample.values():
    val=fix_teen(val)
    sum+=val
print(sum)

  
 
    
    