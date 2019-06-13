# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:33:49 2019

@author: DiPu
"""

li=[]
print("enter no of elements:")
no=int(input())
for  i in range(1,no+1):
    item=int(input())
    li.append(item)
i=no
sum=0
while i<0:
    if li[i]==13:
        i=i+2
        continue
    else:
        sum+=li[i]
        i=i+1
print("sum is:",sum)
    
        
        
