# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:09:59 2019

@author: DiPu
"""
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer 
#reading json file
train=pd.read_json("training_data.json",lines=True)
test=pd.read_json("test_data.json",lines=True)
corpus=[]  
for i in range(0,20217):
    head = re.sub('[^a-zA-Z]', ' ', train['heading'][i])
    head = head.lower()
    head = head.split()
    head = [word for word in head if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    head = [ps.stem(word) for word in head]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    head = ' '.join(head)
    corpus.append(head)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels=train.iloc[:,0].values
features=np.append(features,train.loc[:,['city','section']].values,axis=1)

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,-1 ] = labelencoder.fit_transform(features[:, -1])
features[:,-2 ] = labelencoder.fit_transform(features[:, -2])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1])
features = onehotencoder.fit_transform(features).toarray()

# Avoiding the Dummy Variable Trap
# dropping first column

features = features[:, 1:]


onehotencoder = OneHotEncoder(categorical_features = [-1])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]


#finding features test
corpus1=[]  
for i in range(0,15370):
    head = re.sub('[^a-zA-Z]', ' ', test['heading'][i])
    head = head.lower()
    head = head.split()
    head = [word for word in head if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    head = [ps.stem(word) for word in head]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    head = ' '.join(head)
    corpus1.append(head)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features_test = cv.fit_transform(corpus1).toarray()
features_test=np.append(features_test,test.loc[:,['city','section']].values,axis=1)

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features_test[:,-1 ] = labelencoder.fit_transform(features_test[:, -1])
features_test[:,-2 ] = labelencoder.fit_transform(features_test[:, -2])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [-1])
features_test = onehotencoder.fit_transform(features_test).toarray()
# Avoiding the Dummy Variable Trap
# dropping first column
features_test = features_test[:, 1:]

onehotencoder = OneHotEncoder(categorical_features = [-1])
features_test = onehotencoder.fit_transform(features_test).toarray()
features_test = features_test[:, 1:]



from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features, labels)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)
print(labels_pred)

tmp=pd.DataFrame(labels_pred)
tmp[0].value_counts()[:2].plot.bar()



