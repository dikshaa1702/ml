
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:13:45 2019

@author: DiPu
"""

import pandas as pd
dt=pd.read_csv("telecom_churn.csv")
#satisfying both conditions using and
dt_sub=dt[(dt['voice mail plan']=='yes') &\
          (dt['international plan']=='yes')]

print("count of Churned customer availing both voice mail plan and international plan schema:",dt_sub['voice mail plan'].value_counts()[0])
print("total charge for not churned international call",dt.groupby('churn')['total intl calls'].sum()[0])
print("total charge for  churned international call",dt.groupby('churn')['total intl calls'].sum()[1])

pie1 =(dt.groupby('churn')['total intl calls'].sum()).plot.pie(autopct='%1.1f%%')
#state having max night calls
max_nyt_call=dt['total night minutes'].max()
state_name=dt[(dt['total night minutes']==max_nyt_call)]['state'].iloc[0]
print("state having max night calls:",state_name)

#the most popular call type among churned user
call_analysis = dt.iloc[:, 7:19].sum().sort_index()
visual_2 = call_analysis.plot.bar()



#Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
customer_care = dt['customer service calls'].value_counts()
print(customer_care)

#In which area code the international plan is most availed?
area_people = dt.groupby('area code')['international plan'].value_counts().unstack()
print(area_people)
