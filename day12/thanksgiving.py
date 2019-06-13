# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:14:48 2019

@author: DiPu
"""

import pandas as pd
dt=pd.read_csv("thanksgiving.csv",encoding="Windows 1252")
print("region based dishes",dt.groupby('US Region')['What is typically the main dish at your Thanksgiving dinner?'].value_counts())
print("income based :",dt.groupby('How much total combined money did all members of your HOUSEHOLD earn last year?')['What is typically the main dish at your Thanksgiving dinner?'].value_counts())

#converting coljmn names

dt.renamcolumns={'RespondentID':'ID',"Do you celebrate Thanksgiving?":"CELEBRATE","What is typically the main dish at your Thanksgiving dinner?":"main dish" \
                   "What is typically the main dish at your Thanksgiving dinner? - Other (please specify)":"main dish1","How is the main dish typically cooked?":"way_to_cook" \
                  "How is the main dish typically cooked? - Other (please specify)":"way_to_cook1" })