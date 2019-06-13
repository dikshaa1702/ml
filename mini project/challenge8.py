# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:43:28 2019

@author: DiPu
"""

import random
import re
guess=random.randrange(1,11)
print("enter number")
no=int(input())
if re.findall(r'[0-9]',no):
    if guess==no:
        print("matched")
    else:
        print("enter valid input")