# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:58:57 2019

@author: DiPu
"""

import pandas as pd
data=pd.read_csv("Dating_Data.csv", encoding="Windows 1252")
features=data.iloc['pf_o_att','pf_o_sin','pf_o_int','pf_o_fun','pf_o_amb','pf_o_sha'].values
