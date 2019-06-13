# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:12:39 2019

@author: DiPu
"""

list1=[
 "34587, Learning Python, Mark Lutz, 4 ,40.95",
    "98762,Programming Python, Mark Lutz, 5 ,56.80",
    "77226, Head First Python, Paul Barry 3 ,32.95",
    "88112 ,Einführung in Python3, Bernd Klein , 3 ,24.99 "]
a=[item.split(',') for item in list1]
li1=[]
for items in a:
        li1.append(items[-1])
li2=[]
for items in a:
#    for words in items:
    li2.append(items[0])
li3=[]
for item in li1:
    li3.append(float(item))
li4=[]
for items in li3: 
   if items<100.0:
    li4.append(items+10)
   else:
       continue
zipped=zip(li2,li4)
li5=list(zipped)
print(li5)


        
