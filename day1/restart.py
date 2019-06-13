# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:06:37 2019

@author: DiPu
"""

str1="RESTART"
l=str1.find('R')
a=str1[:l+1]
b=str1[l+1:]
print(a+b.replace('R','$'))
 
    
    