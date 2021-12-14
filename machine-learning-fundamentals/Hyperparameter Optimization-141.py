## 1. Recap ##

import pandas as pd

train_df=pd.read_csv('dc_airbnb_train.csv')

test_df=pd.read_csv('dc_airbnb_test.csv')

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import math
hyper_params=list(range(1,6))
mse_values=[]
col=['accommodates','bedrooms','bathrooms','number_of_reviews']
for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i, algorithm='brute')

    knn.fit(train_df[col],train_df['price'])

    all_features_predictions=knn.predict(test_df[col])
    mse_values.append(mean_squared_error(all_features_predictions,test_df['price']))
    
print(mse_values)

## 3. Expanding grid search ##

hyper_params=list(range(1,21))
mse_values=[]
col=['accommodates','bedrooms','bathrooms','number_of_reviews']
for i in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=i, algorithm='brute')

    knn.fit(train_df[col],train_df['price'])

    all_features_predictions=knn.predict(test_df[col])
    mse_values.append(mean_squared_error(all_features_predictions,test_df['price']))
    
print(mse_values)

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(x=hyper_params,y=mse_values)
plt.show()

## 5. Varying Hyperparameters ##

import matplotlib.pyplot as plt

features = [a for a in train_df.columns if a!='price']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(x=hyper_params,y=mse_values)
plt.show()

## 6. Practice the workflow ##

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]
# Append the first model's MSE values to this list.
import matplotlib.pyplot as plt

# features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
two_mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[two_features], train_df['price'])
    predictions = knn.predict(test_df[two_features])
    mse = mean_squared_error(test_df['price'], predictions)
    two_mse_values.append(mse)

    
hyper_params = [x for x in range(1, 21)]
three_mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[three_features], train_df['price'])
    predictions = knn.predict(test_df[three_features])
    mse = mean_squared_error(test_df['price'], predictions)
    three_mse_values.append(mse)
    
two_hyp_mse = {two_mse_values.index(min(two_mse_values))+1:min(two_mse_values)}
three_hyp_mse = {three_mse_values.index(min(three_mse_values))+1:min(three_mse_values)}