# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:44:11 2019

@author: DiPu
"""

def days_in_months(month,year):
    list1=['jan','feb','march','april','may','june','july','august','sept','oct','nov','dec']
    if month =='jan' or month=='march' or month=='may' or month=='july' or month=='august' or month=='oct' or month=='dec':
        print("31 days")
    elif month =='april' or month=='sept' or month=='nov' or month=='june':
        print("30 days")
    elif month =='feb' and year%4==0 or (year%100==0 and year%400==0):
        print("29 days")
    elif month =='feb' and year%4!=0 or year%400!=0 and year%100==0:
        print("28 days")
days_in_months('feb',2016)      
    