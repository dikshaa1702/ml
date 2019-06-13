# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:46:11 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("election.csv")
#df=data.groupby('State')[['Constituency','%','Party']].max()

df1=data[['State','Constituency','%','Party']]
df1_sort=df1.sort_values(by='%',ascending=False)
df_final=df1_sort.drop_duplicates(subset='Constituency')
print(df_final)
df_final.head(2).plot.bar()


df_raj=df1[df1['State'] == 'Rajasthan' ][['Party','%','Constituency']]
raj_sort=df_raj.sort_values(by='%',ascending=False)
raj_final=raj_sort.drop_duplicates(subset='Constituency')
print(raj_final)

#Visualize the total seats gained by each party in each states.
df2=data[["State","%","Party",'Constituency']]
df2_sort=df2.sort_values(by='%',ascending=False)
df2_final=df2_sort.drop_duplicates(subset='Constituency')
print(df2_final.groupby(["State","Party"])["Constituency"].count())

#4. Visualize the total seats won by the parties in the whole country
df2=data[["State","%","Party",'Constituency']]
df2_sort=df2.sort_values(by='%',ascending=False)
df2_final=df2_sort.drop_duplicates(subset='Constituency')
df2_final['Party'].value_counts()


