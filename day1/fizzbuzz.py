# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:24:13 2019

@author: DiPu
"""
for i in range(1,101):
    if (i%3==0 and i%5==0):
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)