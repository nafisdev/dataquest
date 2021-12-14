## 2. Introduction To The Data ##

import pandas as pd


data=pd.read_csv('AmesHousing.txt',delimiter='\t')

train=data.iloc[:1460,:]

test=data.iloc[1460:,:]
target='SalePrice'

## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
fig= plt.figure(figsize=[7,15])
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

train.plot(x="Garage Area", y="SalePrice", ax=ax1, kind="scatter")
train.plot(x="Gr Liv Area", y="SalePrice", ax=ax2, kind="scatter")
train.plot(x="Overall Cond", y="SalePrice", ax=ax3, kind="scatter")
plt.show()

## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression
import numpy as np

# X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = np.dot(X, np.array([1, 2])) + 3
# print(train[['Garage Area', 'Gr Liv Area', 'Overall Cond', 'SalePrice']].corr())
reg = LinearRegression().fit(train[['Gr Liv Area']], train[['SalePrice']])

a0=float(reg.intercept_)
a1=reg.coef_[0]

## 6. Making Predictions ##

import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

train_rmse=sqrt(mean_squared_error(train[['SalePrice']], lr.predict(train[['Gr Liv Area']])))
test_rmse=sqrt(mean_squared_error(test[['SalePrice']], lr.predict(test[['Gr Liv Area']])))

## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
lr = LinearRegression()
lr.fit(train[cols], train['SalePrice'])

train_rmse_2=sqrt(mean_squared_error(train[['SalePrice']], lr.predict(train[cols])))
test_rmse_2=sqrt(mean_squared_error(test[['SalePrice']], lr.predict(test[cols])))