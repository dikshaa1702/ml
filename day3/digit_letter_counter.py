# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:33:46 2019

@author: DiPu
"""
import re
text=input()
match=re.match(r"([a-z]+)([0-9]+)",text,re.I)
if match:
    items=match.groups()

print(items)
li=[]
for item in items:
    li.append(item)
print(li)
print("character is:",len(li[0]))
print("integer is:",len(li[1]))

      
