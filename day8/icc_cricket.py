# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:32:55 2019

@author: DiPu
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict
odi="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(odi).text
soup = BeautifulSoup(source,"lxml")
right_table=soup.find('table', class_="table")
print(right_table)
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())

col_name = ["ranking","country","weighted match","points","Ratings"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,]))
df = pd.DataFrame(col_data) 
