## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]
# data.head()
data.info()
# numerical_train=['']
numerical_train = train.select_dtypes(include=['int', 'float'])
numerical_train = numerical_train.drop(['PID', 'Year Built', 'Year Remod/Add', 'Garage Yr Blt', 'Mo Sold', 'Yr Sold'], axis=1)
null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series == 0]
print(full_cols_series)

## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]

# from sklearn.linear_model import LinearRegression
# import numpy as np

# # X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# # y = np.dot(X, np.array([1, 2])) + 3
# # print(train[['Garage Area', 'Gr Liv Area', 'Overall Cond', 'SalePrice']].corr())
# for a in full_cols_series:
#     reg = LinearRegression().fit(train[[col]], train[['SalePrice']])

# a0=float(reg.intercept_)
# a1=reg.coef_[0]

sorted_corrs=train_subset.corr()['SalePrice'].apply(lambda x:abs(x)).sort_values()

## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt

strong_corrs=sorted_corrs[sorted_corrs.apply(lambda x:x>0.3)]
corrmat=train_subset[strong_corrs.index]

sns.heatmap(corrmat.corr(),vmin=0, vmax=1)

## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'
clean_test=test[final_corr_cols.index].dropna()
lr = LinearRegression()
lr.fit(train[features], train['SalePrice'])

train_predictions = lr.predict(train[features])
test_predictions = lr.predict(clean_test[features])

train_mse = mean_squared_error(train_predictions, train[target])
test_mse = mean_squared_error(test_predictions, clean_test[target])

train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

print(train_rmse)
print(test_rmse)

## 5. Removing Low Variance Features ##

unit_train = (train[features] - train[features].min())/(train[features].max() - train[features].min())
print(unit_train.min())
print(unit_train.max())

## 6. Final Model ##

clean_test = test[final_corr_cols.index].dropna()
features=features.drop('Open Porch SF')
lr = LinearRegression()
lr.fit(train[features], train['SalePrice'])

train_predictions = lr.predict(train[features])
test_predictions = lr.predict(clean_test[features])

train_mse = mean_squared_error(train_predictions, train[target])
test_mse = mean_squared_error(test_predictions, clean_test[target])

train_rmse_2 = np.sqrt(train_mse)
test_rmse_2 = np.sqrt(test_mse)

print(train_rmse_2)
print(test_rmse_2)