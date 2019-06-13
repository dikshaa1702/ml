# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:47:13 2019

@author: DiPu
"""
s=input()
i= len(s)
a=s[0]
b=s[i-1]
c=s[1:i-1]
print(a+c.replace('','*')+b)
    