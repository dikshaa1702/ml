# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:27:08 2019

@author: DiPu
"""

import pandas as pd

df = pd.read_csv("data.csv")

feat = df.iloc[:,:-1].values
lab = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split as TTS

f_tr,f_te, l_tr, l_te = TTS(feat, lab, test_size=0.2, random_state=0)


from sklearn.preprocessing import LabelEncoder

cols = [4,5,6]
objs = []

for col in cols:
    le = LabelEncoder()
    f_tr[:,col] = le.fit_transform(f_tr[:,col])
    objs.append(le)

view = pd.DataFrame(f_te)


for col, obj in zip(cols,objs):
    f_te[:,col] = obj.transform(f_te[:,col])