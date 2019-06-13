# -*- coding: utf-8 -*-
"""
Created on Sun May 26 12:43:45 2019

@author: DiPu
"""

import pandas as pd
df=pd.read_csv("ign.csv")
ign_df = df.iloc[:,1:]

df_xbox= df[(ign_df['platform'] =='Xbox') & \
           (df['score'] > 7) ]

df_games=df.groupby('platform')['score_phrase'].value_counts().unstack().fillna(0)

xbox_visual = ign_df['score'][ign_df['platform']=="Xbox One"].plot.hist()
ps4_visual = df['score'][df['platform']=="PlayStation 4"].plot.hist()
