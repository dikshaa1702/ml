# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:30:18 2019

@author: DiPu
"""

import random
guess=random.randrange(1,11)
print("enter number")
no=int(input())
if(guess==no):
    print("player wins and computer lose")
else:
    print("player lose and computer wins")
print("random no: {0}".format(guess,no))
print("guess no: {1}".format(guess,no))
if no==guess:
    print("guess write")
elif ((no<=guess+2) or (no>=guess-2)):
    print("too high")
else:
    print("too low")
    while guess!=no:
    print("enter number")
    no=int(input())
print("guess matched")   