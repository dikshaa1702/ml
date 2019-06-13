# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:05:54 2019

@author: DiPu
"""
list1=[[34587, 'Learning Python', 'Mark Lutz', 4 ,40.95],
    [98762,'Programming Python', 'Mark Lutz', 5 ,56.80],
    [77226, 'Head First Python', 'Paul Barry', 3 ,32.95],
    [88112 ,'Einführung in Python3', 'Bernd Klein' , 3 ,24.99 ]]


min=100
eq=list(map((lambda x:x if x[-1]>=min else (x[0],x[-1]+10)),map(lambda x:(x[0],x[-1]),list1)))
