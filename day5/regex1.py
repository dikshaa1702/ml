# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:42:52 2019

@author: DiPu
"""
def floatno(no):
    import re
    if re.findall(r'[+-]?[0-9]{1,}+[0-9]{1,}',no):
        print("true")
    else:
        print("false")
ip=input().split()
floatno(ip)



