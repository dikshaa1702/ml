# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:49:25 2019

@author: DiPu
"""

list1 = []
while True:
    user_input = input("Enter name, age and score: ")
    if not user_input:
        break
    name, age, marks = user_input.split(",")
    list1.append((name,int(age),int(marks)))
list1.sort()
print(list1)
        