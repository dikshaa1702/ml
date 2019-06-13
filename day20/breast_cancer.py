# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:03:15 2019

@author: DiPu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("breast_cancer.csv")
data['G']=data['G']