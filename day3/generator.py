# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:11:18 2019

@author: DiPu
"""
li=[]
print("enter total no of elements")
no=int(input())
for  i in range(1,no+1):
    item=int(input())
    li.append(item)
print(li)
print(tuple(li))
    