#Project to make a machine learning model to predict the weekly sales of Walmart in US
"""
We are given some weekly sales of the Walmart at 45 stores having 98 products.
We need to predict the weekly sales at given stores on given dates according to the given features.
"""

#import basic libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


#read all the given data and make dataframe for each data

features_df=pd.read_csv('features.csv')
sample_submission_df=pd.read_csv('sampleSubmission.csv')
stores_df=pd.read_csv('stores.csv')
test_df=pd.read_csv('test.csv')
train_df=pd.read_csv('train.csv')



#replace nan values with 0
features_df=features_df.replace(np.nan, 0)

#merge type and size of store in the features for each store
features_with_stores=pd.merge(features_df, stores_df, on=['Store'], how='inner')

#adding features to the train data
merge_df=pd.merge(train_df, features_with_stores, on=['Store','Date','IsHoliday'], how='inner')

#Handling date 
from datetime import datetime as dt
merge_df['DateTimeObj']=[dt.strptime(x,'%Y-%m-%d') for x in list(merge_df['Date'])]

#plotting weekly sales according to date
plt.plot(merge_df[(merge_df.Store==30)].DateTimeObj, merge_df[(merge_df.Store==30)].Weekly_Sales, 'ro')
plt.show()

#calculate weekly sales for each store
weekly_sales_by_store = merge_df.groupby(['Store','Date'])['Weekly_Sales'].apply(lambda x:np.sum(x))
Total_Sales_foreach_dept = merge_df.groupby(['Store','Dept'])['Weekly_Sales'].apply(lambda x:np.sum(x))

#Managing the index
weeklyscale_by_store=weekly_sales_by_store.reset_index()
Total_sale_by_dept = Total_Sales_foreach_dept.reset_index()
"""
In walmart store, only 'weekly sales' column is added
we are working on the training data
"""

#Merging the weekly sales of each store with features(including type & size)
Walmart_Store = pd.merge(weeklyscale_by_store,features_with_stores, on =['Store','Date'],how='inner')
Walmart_Store.reset_index()

#handle dates
Walmart_Store['DateTimeObj']=[dt.strptime(x,'%Y-%m-%d') for x in list(Walmart_Store['Date'])]
Walmart_Store["DateO"] = Walmart_Store['DateTimeObj'].apply(lambda x: x.toordinal())
Walmart_Store=Walmart_Store.drop(['DateTimeObj','Date',], axis=1)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

Walmart_Store['IsHoliday']=le.fit_transform(Walmart_Store['IsHoliday'])
Walmart_Store['Type']=le.fit_transform(Walmart_Store['Type'])


filename = 'label_encode.pickle'
pickle.dump(le, open(filename, 'wb'))

pout=open(filename,'rb')
exp=pickle.load(pout)

#train test split
from sklearn.model_selection import train_test_split
WM_features=Walmart_Store.iloc[:,list(range(1))+list(range(2,15))]
WM_labels=Walmart_Store.iloc[:,1]

train_ft_WM, test_ft_WM , train_lb_WM, test_lb_WM= train_test_split(WM_features, WM_labels, test_size=0.3,random_state=42)


 
#standard scaling
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
train_df_WM=scaler.fit_transform(train_ft_WM)
test_df_WM=scaler.fit_transform(test_ft_WM)

#precdict 
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(train_df_WM, train_lb_WM)
labels_pred_WM=regressor.predict(test_df_WM)

regressor.score(test_df_WM, test_lb_WM)

#prediction using random forest generator because avg score is 94 ,for decision tree avg score is 93,
#and for linear regression it is 70
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(train_df_WM, train_lb_WM)  
labels_pred = regressor.predict(test_df_WM)  
regressor.score(test_df_WM, test_lb_WM)


#finding mean score using k fold cross validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = regressor, X =train_df_WM , y =train_lb_WM , cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())


#adding features to the test data
merge_df_test=pd.merge(test_df, features_with_stores, on=['Store','Date','IsHoliday'], how='inner')

#handle dates
merge_df_test['DateTimeObj']=[dt.strptime(x,'%Y-%m-%d') for x in list(merge_df_test['Date'])]
merge_df_test["DateO"] = merge_df_test['DateTimeObj'].apply(lambda x: x.toordinal())
merge_df_test=merge_df_test.drop(['DateTimeObj','Date','Dept'], axis=1)
#label encoding test data
from sklearn.preprocessing import LabelEncoder
le1=LabelEncoder()

merge_df_test['IsHoliday']=le.fit_transform(merge_df_test['IsHoliday'])
merge_df_test['Type']=le.fit_transform(merge_df_test['Type'])
#finding prediction for test data
test_pred=regressor.predict(merge_df_test)


filename = 'WalmartSales.py'
pickle.dump(regressor, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(merge_df_test)
print(result)

