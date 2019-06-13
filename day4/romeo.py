# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:48:12 2019

@author: DiPu
"""

file=open("romeo.txt")

counts = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
