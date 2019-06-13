# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:22:59 2019

@author: DiPu
"""
dic={}
text=input()
for keys in text:
    dic[keys]=dic.get(keys,0)+1
print(dic)
