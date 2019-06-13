# -*- coding: utf-8 -*-
"""
Created on Tue May  7 19:44:22 2019

@author: DiPu
"""
import random
guess=random.randrange(1,11)
print(guess)
print("enter number")
no=int(input())
if no==guess:
    print("guess write")
elif ((no<=guess+2) or (no>=guess-2)):
    print("too high")
else:
    print("too low")
