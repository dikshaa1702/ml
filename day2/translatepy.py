# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:43:22 2019

@author: DiPu
"""

def translate(text):
    import string
    li=['a','e','i','o','u','A','I','O','E','U']
    li1=[]
    for i in text:
        if i not in li:
            li1.append(i+'o'+i)
        else:
            li1.append(i)
    print(''.join(li1))
translate("diksha")            
    