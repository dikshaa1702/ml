# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:04:17 2019

@author: DiPu
"""
from  functools import reduce
ip=[ int(x)  for x in input().split()]
filter_list=reduce(lambda a,b:a+b,list((filter(lambda x:x%2==1,ip))))
