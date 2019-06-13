# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:29:45 2019

@author: DiPu
"""
from collections import OrderedDict
od=OrderedDict()
    
while True:
    user_inp = input("Enter Product: ")
    if user_inp == "":
        break
    user_inp = user_inp.split()
    key = " ".join(user_inp[:-1])
    value = int(user_inp[-1])
    od[key] = od.get(key,0)+value
print(od)    
    
#for key,value in od.items():
#    if "apple" in od.keys():
#        od["apple"] = od["apple"]+20
#    else:
#        od["apple"] = 20

    

    
        
