# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:04:12 2019

@author: DiPu
"""

import random
guess=random.randrange(1,11)
i=6
while guess!=no and i!=0:
    print("enter number")
    no=int(input())
    i=i-1
    print("no of chances left:",i)
print("you have reached max limit of guess")   