# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:26:49 2019

@author: DiPu
"""
import csv
list1=[]
list2=[]
list3=[]
with open("population.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        list1.append(row[2])
        list2.append(row[1])
        list3.append(row[3])
for items in list1:
    for i in items:
        i.replace(',','')
li=[int(x) for x in list1]
dict1={}
if item not in dict1:
    
