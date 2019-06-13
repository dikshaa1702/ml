# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:55:04 2019

@author: DiPu
"""
from functools import reduce
list1= [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), list1))
total=list(map(lambda x:[x[0]]+list(reduce(lambda a,b:a+b,x[1:])),invoice_totals))

