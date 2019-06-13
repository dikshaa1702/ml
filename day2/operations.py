# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:30:22 2019

@author: DiPu
"""

def add(li):
    sum=0
    for item in li:
        sum=sum+item
    return sum
        
def mult(li):
    m=1
    for item in li:
       m =m*item
    return m
def large(li):
    sort(li)
    return li[-1]  
def small(li):
    sort(li)
    return li[0]  
def sort(li):
    li.sort()
    return li
def remove_dup(li):
    li=list(dict.fromkeys(li))
    return li
li=[]
for  i in range(1,6):
    item=int(input())
    li.append(item)
print("sum is:",add(li))
print("multiple is:",mult(li))
print("smallest is:",small(li))
print("largest is:",large(li))
print("sorted list is:",sort(li))
print("remove dup:",remove_dup(li))
    
        