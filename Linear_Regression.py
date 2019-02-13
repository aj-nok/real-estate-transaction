from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import cross_validation
import pandas as pd
import numpy as np 
model = LinearRegression()

df=pd.read_csv("realestatetransactions_new.csv")


X=df['sq__ft']
Y=df['price']
X=X.values.reshape(len(X),1)
Y=Y.values.reshape(len(Y),1)


#X_train = X[:-250]                        # Split the targets into training/testing sets Manually
#X_test = X[-250:]
#Y_train = Y[:-250]
#Y_test = Y[-250:]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)    #Split the targets into training/testing sets Randomly

model.fit(X_train, Y_train)
plt.scatter(X_test, Y_test,  color='black')
plt.title('Test Data')
plt.xlabel('Size')
plt.ylabel('Price')
plt.xticks(())
plt.yticks(())

plt.plot(X_test, model.predict(X_test), color='red',linewidth=3)
plt.show()
print(model.predict(X_test))
