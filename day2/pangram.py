# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:09:07 2019

@author: DiPu
"""
def pangram(str1):
    import string
    a_z=string.ascii_lowercase
    for j in a_z:
        if j not in str1.lower():
            return False
        else:
            return True
data= input()
if pangram(data):
    print("pangram")
else:
    print("not pangram")