# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:53:54 2019

@author: DiPu
"""
import pandas as pd
df = pd.read_csv("training_titanic.csv")
#value_counts used for counting rows

print("total survived:",df['Survived'].value_counts()[1])
print("total died:",df['Survived'].value_counts()[0])

#normalize fuction used for returning values in percentage form
print("total percentage survived",df['Survived'].value_counts(normalize = True)[1]*100)
print("total percentage died",df['Survived'].value_counts(normalize = True)[0]*100)





df_survm= df[(df['Sex'] =='male') & \
           (df['Survived'] == 1) 
            ]
print("total male survived:",df_survm['Sex'].value_counts()[0])

df_diedm= df[(df['Sex'] =='male') & \
           (df['Survived'] == 0) 
            ]
print("total male died:",df_diedm['Sex'].value_counts()[0])


df_survf= df[(df['Sex'] =='female') & \
           (df['Survived'] == 1) 
            ]
print("total female survived:",df_survf['Sex'].value_counts()[0])

df_diedf= df[(df['Sex'] =='female') & \
           (df['Survived'] == 0) 
            ]
print("total female died:",df_diedf['Sex'].value_counts()[0])

