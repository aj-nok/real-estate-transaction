# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:18:01 2019

@author: aj-nok
"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
from sklearn.metrics import r2_score
import tkinter as tk 
import pandas as pd
import numpy as np 
model = LinearRegression()

df=pd.read_csv('realestatetransactions.csv',usecols=["sq__ft","latitude","longitude","beds","baths","price"])
df = df[df.sq__ft != 0]
X = np.column_stack((df['sq__ft'],df['beds'],df['baths']))
Y=df['price']
Y=Y.values.reshape(len(Y),1)
model.fit(X, Y)

print('Intercept: \n', model.intercept_)
print('Coefficients: \n', model.coef_)

X = sm.add_constant(X) 
mod = sm.OLS(Y, X).fit()
predictions = mod.predict(X) 
root= tk.Tk() 
root.title("Prediction")
 
canvas1 = tk.Canvas(root, width = 1200, height = 450)
canvas1.pack()


print_mod = mod.summary()
label_model = tk.Label(root, text=print_mod, justify = 'center', relief = 'solid', bg='yellow')
canvas1.create_window(800, 220, window=label_model)

label0 = tk.Label(root, text='Enter the details: ')
canvas1.create_window(80, 80, window=label0)
label1 = tk.Label(root, text='Type Square feet: ')
canvas1.create_window(100, 100, window=label1)
entry1 = tk.Entry (root) 
canvas1.create_window(270, 100, window=entry1)
label4 = tk.Label(root, text=' Type Beds: ')
canvas1.create_window(120, 120, window=label4)
entry4 = tk.Entry (root) 
canvas1.create_window(270, 120, window=entry4)
label5 = tk.Label(root, text=' Type Baths: ')
canvas1.create_window(140, 140, window=label5)
entry5 = tk.Entry (root) 
canvas1.create_window(270, 140, window=entry5)

def values(): 
    global New_sq__ft_Rate 
    New_sq__ft_Rate = int(entry1.get()) 
    global New_beds_Rate 
    New_beds_Rate = int(entry4.get())  
    global New_baths_Rate 
    New_baths_Rate = int(entry5.get()) 
    Prediction_result  = ('Predicted  Price: ', model.predict([[New_sq__ft_Rate,New_beds_Rate,New_baths_Rate]]))
    label_Prediction = tk.Label(root, text= Prediction_result, font=("times", 21), bg='red')
    canvas1.create_window(260, 280, window=label_Prediction)
    
button1 = tk.Button (root, text='Predict  Price',command=values, bg='cyan') 
canvas1.create_window(270, 210, window=button1)
root.mainloop()
