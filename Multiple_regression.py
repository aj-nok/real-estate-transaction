# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:48:51 2019

@author: ajas
"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np 
model = LinearRegression()

df=pd.read_csv('realestatetransactions.csv',usecols=["sq__ft","latitude","longitude","beds","baths","price"])
df = df[df.sq__ft != 0]                                         #Getting numeric fields only    
df = (df - df.mean())/df.std()                                  #DATA Normalization


X = np.column_stack((df['sq__ft'],df['beds'],df['baths'],df['latitude'],df['longitude']))
#X=df[['sq__ft']]
Y=df['price']
#X=X.values.reshape(len(X),1)
Y=Y.values.reshape(len(Y),1)

#model.fit(X, Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=11)
model.fit(X_train, Y_train)                                    #Split the targets into training/testing sets
Y_pred_ml = model.predict(X_test)

print('r2 value: ', r2_score(Y_test, Y_pred_ml))
print('Intercept: ', model.intercept_)                  
print('Coefficients: ', model.coef_)
X = sm.add_constant(X)                                           #Applying Ordinary Least Squares
mod = sm.OLS(Y, X).fit()
predictions = mod.predict(X) 
print_mod = mod.summary()
print(print_mod)


