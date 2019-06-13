# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:32:32 2019

@author: DiPu
"""



file = open("absentee.txt", "wt")
max=25
flag=0
while True and max<=25:
    i=input("enter name:")
    if i=='':
        break
    
    file.write(i)
    flag=flag+1
    if flag==max:
        break
file.close()
file= open("absentee.txt", "rt")
print(file.readline())
    
    