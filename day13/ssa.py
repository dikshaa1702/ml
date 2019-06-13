# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:54:56 2019

@author: DiPu
"""
import os
import pandas as pd
path = os.getcwd()
files = os.listdir(path)
#adding all txt file in a list
li1=[]
df=pd.DataFrame(columns = ['Name', 'Sex', 'Number','Year'])
for i in range(0,len(files)):
   temp=files[i].split('.')
   if temp[-1]=='txt':
       li1.append(files[i])
#all files from 1880 to 2010
for i in range(1880,2011):
    for x in li1:
        if x =="yob"+str(i)+".txt":
           df2 = pd.read_csv(x,header=None)
           df2.columns = ['Name', 'Sex', 'Number']
           df2['Year']=i
           df2 = df2.sort_values(by=['Number'], ascending=False)
           df=pd.concat([df, df2])
#for column 2010 split the string in order to get the name of babies and head method for top 5 babies
print("Top 5 male baby name in 2010\n",df[(df["Sex"] == "M") & (df["Year"] == 2010)].head(5))
print("Top 5 female baby name in 2010\n",df[(df["Sex"] == "F") & (df["Year"] == 2010)].head(5))
#unstack method is used to make idex values into column names
df=df.groupby(['Year', 'Sex'])['Number'].aggregate('sum').unstack()
df.plot()
        