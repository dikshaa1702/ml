# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:53:49 2019

@author: DiPu
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
link="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source=requests.get(link).text
soup=BeautifulSoup(source,'lxml')
#reading html code of table in which it is stored
right_table=soup.find('table', class_="wikitable")
state=[]
national_share=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells)==7:
        state.append(cells[1].text.strip())
        national_share.append(cells[4].text.strip())
#convert list values which is in string into float
values=([ float(x) for x in national_share])
explode = (0.5,0,0,0,0,0,0)
plt.pie(values[0:7], explode = explode, labels=state[0:7], autopct='%2.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()