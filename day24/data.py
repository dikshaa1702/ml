# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:02:22 2019

@author: DiPu
"""
# Impoimport numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Importing the dataset (Bivariate Data Set with 3 Clusters)
data = pd.read_csv('data.csv')
data=data.drop(['Subregion','Locale','Locus','Excavation','River','Period','Dynasty','Reign','Portfolio','Artist Suffix'],axis=1)

#Visualize the various countries from where the artworks are coming.
country=data[data.Country.notnull()]
#plot pie chart of different countries for their art work
data['Country'].value_counts().plot.pie()

#Visualize the top 2 classification for the artworks
data['Classification'].value_counts().head(2).plot.bar()

#Visualize the artist interested in the artworks
data['Artist Display Name'].dropna()
data['Artist Display Name'].value_counts()[:20].plot.bar()


#Visualize the top 2 culture for the artworks
culture=data[data.Culture.notnull()]
culture['Culture'].value_counts()[:2].plot.bar()

list1=data["Country"].value_counts()
labels=list1.index
value=list1.values
patches, texts = plt.pie(value, startangle=90, radius=1)
plt.legend(patches, labels, loc='best', 
           fontsize=8)


