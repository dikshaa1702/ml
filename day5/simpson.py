# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:03:57 2019

@author: DiPu
"""

import re
fp=open("simpsons_phone_book.txt",'rt')
for items in fp:
        if re.search(r"J.*Neu",items):
            print(items.rstrip())
fp.close()