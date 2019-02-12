# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:38:26 2019

@author: aj-nok

about: Data Visualization using pandas,numpy,matplotlib

dataset: realesatatetransactions.csv
"""

#CODE:

import pandas as pd
import numpy as np
import matplotlib.pyplot as mplt
import seaborn as sns

data=pd.read_csv("realestatetransactions.csv")      

city_count=data['city'].value_counts()                                                    #BAR GRAPH
city_count.plot(kind='bar', title='BAR Graph between cities and their counts:') 
type_count=data['type'].value_counts()
type_count.plot(kind='bar',title='BAR Graph between type and their counts:')


cityprice_sacramento = data['price'][data['city']=='SACRAMENTO']                          #BOX PLOT: TOP CITIES VS PRICE
cityprice_elkgrove = data['price'][data['city']=='ELK GROVE']
cityprice_lincoln = data['price'][data['city']=='LINCOLN']
cityprice_roseville = data['price'][data['city']=='ROSEVILLE']
cityprice_citrusheights = data['price'][data['city']=='CITRUS HEIGHTS']
cityprice_antelope = data['price'][data['city']=='ANTELOPE']
cityprice_ranchocordova = data['price'][data['city']=='RANCHO CORDOVA']
cityprice_eldoradohills = data['price'][data['city']=='EL DORADO HILLS']
cityprice_galt = data['price'][data['city']=='GALT']
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot([cityprice_sacramento,cityprice_elkgrove,cityprice_lincoln,cityprice_roseville], labels=['SACRAMENTO', 'ELK GROVE','LINCOLN','ROSEVILLE'])
ax.boxplot([cityprice_citrusheights,cityprice_antelope,cityprice_ranchocordova,cityprice_eldoradohills,cityprice_galt], labels=['CITRUS HEIGHTS', 'ANTELOPE','RANCHO CORDOVA','EL DORADO HILLS','GALT'])


citysqft_sacramento = data['sq__ft'][data['city']=='SACRAMENTO']                         #BOX PLOT: TOP CITIES VS SQFT
citysqft_elkgrove = data['sq__ft'][data['city']=='ELK GROVE']
citysqft_lincoln = data['sq__ft'][data['city']=='LINCOLN']
citysqft_roseville = data['sq__ft'][data['city']=='ROSEVILLE']
citysqft_citrusheights = data['sq__ft'][data['city']=='CITRUS HEIGHTS']
citysqft_antelope = data['sq__ft'][data['city']=='ANTELOPE']
citysqft_ranchocordova = data['sq__ft'][data['city']=='RANCHO CORDOVA']
citysqft_eldoradohills = data['sq__ft'][data['city']=='EL DORADO HILLS']
citysqft_galt = data['sq__ft'][data['city']=='GALT']
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('BOX PLOT CITY VS sqft 2')
ax.boxplot([citysqft_sacramento,citysqft_elkgrove,citysqft_lincoln,citysqft_roseville], labels=['SACRAMENTO', 'ELK GROVE','LINCOLN','ROSEVILLE'])
ax.boxplot([citysqft_citrusheights,citysqft_antelope,citysqft_ranchocordova,citysqft_eldoradohills,citysqft_galt], labels=['CITRUS HEIGHTS', 'ANTELOPE','RANCHO CORDOVA','EL DORADO HILLS','GALT'])

plt.scatter(data['price'], data['sq__ft'],  c='blue', alpha=0.5)       #SCATTER PLOT PRICE VS SQFT
plt.title('Scatter plot price vs sqft')
plt.xlabel('price')
plt.ylabel('sq__ft')

plt.scatter(data['price'], data['beds'],  c='red', alpha=0.5)           #SCATTER PLOT PRICE VS BEDS
plt.title('Scatter plot price vs beds')
plt.xlabel('price')
plt.ylabel('beds')

plt.scatter(data['price'], data['baths'],  c='green', alpha=0.5)           #SCATTER PLOT PRICE VS BATHS
plt.title('Scatter plot price vs baths')
plt.xlabel('price')
plt.ylabel('baths')

pd.plotting.scatter_matrix(df, figsize=(6, 6))                    #Correlation Matrix
plt.show()
print(df.corr())
