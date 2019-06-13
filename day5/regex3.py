# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:17:01 2019

@author: DiPu
"""

def valid(card_no):
    import re
    for items in card_no:
        if re.findall(r'([^[4-6]\d{3}(-?\d{4}){3}$)*16',items) and  not re.search(r'(\d)\1{3,}',card_no.replace('-','')):
            print("valid")
        else:
            print("invalid")
ip=input().split()
valid(ip)
 

