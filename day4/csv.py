# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:52:49 2019

@author: DiPu
"""

import csv

with open(' passwd.txt')open('output.csv', 'w') as output:
    r = csv.reader(passwd, delimiter=':')
    w = csv.writer(output, delimiter='\t')
    for record in r:
        if len(record)>1:
            w.writerow((record[0], record[2]))
w1=open(w)
print(w1)