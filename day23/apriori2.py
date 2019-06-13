# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:03:07 2019

@author: DiPu
"""

import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)



transactions = []

for i in range(0, 7501):
    
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

list1=[]
for item in transactions:
    for value in item:
        cleanedlist=[value for value in item if str(value)!='nan']
    list1.append(cleanedlist)   
print("cleaned list:",list1)
#the bar chart of top 10 edibles.
from collections import defaultdict
dict1=defaultdict(int)
for item in list1:
    for value in item:
        dict1[value]+=1
    
list2=sorted(dict1.values)
 



# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)


