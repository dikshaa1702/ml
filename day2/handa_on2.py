# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:41:23 2019

@author: DiPu
"""
def leap_yr(year):
    if(year%4==0) and (year%400!=0):
        print("leap year")
    else:
        print("not a leap year")
leap_yr(2017)