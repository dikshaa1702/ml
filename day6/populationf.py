# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:26:49 2019

@author: DiPu
"""
from collections import defaultdict
import csv
dict1=defaultdict(int)
with open("population.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for items in csv_reader:
          k="India"+ items[-1]
          dict1[k]+=int(items[-2].replace(',',''))
          
print(dict1)
          
    
    
