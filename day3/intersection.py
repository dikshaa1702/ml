# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:45:42 2019

@author: DiPu
"""
li=[int(x) for x in input("enter list1").split()]
print(li)
set1=set(li)
li1=[int(x) for x in input("enter list2").split()]
set2=set(li1)
set3=set1.intersection(set2)
print(list(set3))