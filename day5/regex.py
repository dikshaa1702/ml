# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:55:14 2019

@author: DiPu
"""

def valid(email):
    import re
    li=[]
    for items in email:
        if re.findall(r'[a-z0-9-_]{1,}@+[a-z0-9]{1,}.[a-z]{2,4}',items):
            li.append(items)
        else:
            continue
    print(li)       
ip=input().split()
valid(ip)
