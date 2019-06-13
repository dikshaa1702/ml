# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:02:00 2019

@author: DiPu
"""
def csv_read():
    import csv
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        print(csv_file.readlines(  ))
csv_read()

import csv
li1=[]
li2=[]
dic={}
with open("zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        li1.append(row[0])
        li2.append(row[2])

t1=set(li1)
li2=[int(x) for x in li2]
print(list(t1))
sum1=0
for x in li2:
    sum=sum+x
print("sum is:",sum1)
od={}
for x in range(0,len(li1)):
        if li1[x] in od.keys():
            od[li1[x]]=od[li1[x]]+li2[x]
        else:
            od[li1[x]]=li2[x]
      
print(od)

