# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:14:12 2019

@author: DiPu
"""

import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
dataset = pd.read_csv('amazon_cells_labelled.txt',names=['review','like'], delimiter = '\t')

from nltk.stem.porter import PorterStemmer
corpus=[]

for i in range(0,1000):
    review=re.sub('[^A_Za-z]',' ',dataset['review'][i])
    review=review.lower()
    review=review.split()
    review=[word for word  in review
            if not word in set(stopwords.words('english'))]
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)
#using naive bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)
print(cm_nb)
print("score:",classifier.score(features_test,labels_test))







