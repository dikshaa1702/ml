# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:39:56 2019

@author: DiPu
"""
import re
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("monster_com-job_sample.csv")
loc=data[data["location"].apply(lambda x: str(x).isdigit())]
data=pd.concat([data,loc]).drop_duplicates(keep=False)
#filling nan values by mode values
data["location"]=data["location"].fillna(data["location"].mode()[0])
data["organization"]=data["organization"].fillna(data["organization"].mode()[0])
 
#removing unnecessary description in the column
data=data[data['location'].map(len)<30]
#regex for location


#finding data having location value in organization
lst=[]
for item in data['organization']:
    result=re.findall(r'[A-Za-z]*\s?[[A-za-z]*]?\s?[[A-za-z]*]?[\,]{1}?\s?[A-Z]{2}\s?[0-9]*',item)
    lst.append(result)
    

index=[]
for item in lst:
    if[item!=[]]:
        index.append(lst.index(item))
lst2=[]

for item in index:
    result

