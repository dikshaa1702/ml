# -*- coding: utf-8 -*-
"""
Created on Sun May 12 19:10:03 2019

@author: DiPu
"""
shopping_list=[]
print("enter items to add in list and type quit when you arew done")
while True:
    ip=input("enter list")
    if ip=="QUIT":
        break
    elif ip.upper()=="SHOW":
        print(shopping_list)
    elif ip.upper()=="HELP":
        print("help1:if input is show then items in list will be displayed")
        print("help2:if input is QUIT then total items in list will be printed and user will not be able to add more items")
    else:
        shopping_list.append(ip)
for count,item in enumerate(shopping_list,1):
    print(count,item)
ip=input("enter add to ADDITION/REMOVE of item at some index:")
if ip=="ADDITION":
    ip1=int(input("enter index:"))
    item=input("enter item:")
    shopping_list[ip1-1]=item
elif ip=="REMOVE":
    ip1=int(input("enter index:"))
    shopping_list.pop(ip1-1)
with open("shopping_list_miniprojectpy.py",'rt') as f1:
    with open("shopping.txt",'wt') as f:
        for lines in f1:
            f.write(lines)
ip=open("shopping.txt")
content=ip.readlines()

print(content)
   

    
    
    


    