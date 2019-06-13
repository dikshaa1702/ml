# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:47:16 2019

@author: DiPu
"""

with open ("words.txt", "rt") as rf :
    with open("copy.txt","wt") as wf:
        for line in rf :
            wf.write( line)
            wf.close()
            
content=wf.readlines()
print(content)




    