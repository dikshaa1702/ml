# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:11:20 2019

@author: DiPu

"""
def check(s1,s2):
    if sorted(s1)==sorted(s2):
        print("strings are anagram")
    else:
        print("not anagram")
li=[]
while True:
    inp=input("enter string:")
    if inp=="":
        break
    else:
        li.append(inp)
print(li)
for x,y in zip(li,li[1:]):
    check(x,y)
    
    

        
    