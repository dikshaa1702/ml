# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:02:54 2019

@author: DiPu
"""
import csv
list1=[]
fp=open("population.csv")
for lines in fp:
  list1.append(lines)
list2=[]
for items in list1:
        list2.append(items[0])
