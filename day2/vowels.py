# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:22:08 2019

@author: DiPu
"""

state_name=[ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowel=['A','E','I','O','U','a','e','i','o','u']
final_list = []
for item in state_name:
    item = list(item)
    for letter in vowel:
        while letter in item:
            item.remove(letter)
    final_list.append("".join(item))
print(final_list)

for state in state_name:
    temp_list = []
    for letter in state:
        if letter in vowel:
            continue
        temp_list.append(letter)
    final_list.append("".join(temp_list))