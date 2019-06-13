# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:00:06 2019

@author: DiPu
"""

def acheive(small_brick,big_brick,target):
    if small_brick*1+big_brick*5>=target:
        return True
    else:
        return False
print("enter the values")
small_brick=int(input())
big_brick=int(input())
target=int(input())
if acheive(small_brick,big_brick,target):
    print("True")
else:
    print("False")