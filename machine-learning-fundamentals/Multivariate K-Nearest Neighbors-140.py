## 1. Recap ##

import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings.info()

## 2. Removing features ##

dc_listings=dc_listings.drop(columns=['latitude','longitude','zipcode','state','city','room_type','host_acceptance_rate','host_listings_count','host_response_rate'])

## 3. Handling missing values ##

dc_listings=dc_listings.drop(columns=['cleaning_fee','security_deposit'])


dc_listings.dropna(axis=0, inplace=True)

## 4. Normalize columns ##

dc_listings.head()

normalized_listings=(dc_listings - dc_listings.mean()) / (dc_listings.std())

normalized_listings['price']=dc_listings['price']

print(normalized_listings.head(3))

## 5. Euclidean distance for multivariate case ##

from scipy.spatial import distance

first_fifth_distance=distance.euclidean(list(normalized_listings.loc[574,['accommodates','bathrooms']]),list(normalized_listings.loc[808,['accommodates','bathrooms']]))

print(normalized_listings.head())

## 7. Fitting a model and making predictions ##

from sklearn.neighbors import KNeighborsRegressor

train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]

knn=KNeighborsRegressor(n_neighbors=5,algorithm='brute')

knn.fit(train_df[['accommodates','bathrooms']],train_df['price'])

predictions=knn.predict(test_df[['accommodates','bathrooms']])

## 8. Calculating MSE using Scikit-Learn ##

from sklearn.metrics import mean_squared_error

train_columns = ['accommodates', 'bathrooms']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
knn.fit(train_df[train_columns], train_df['price'])
predictions = knn.predict(test_df[train_columns])

two_features_mse=mean_squared_error(predictions,test_df['price'])
import math
two_features_rmse=math.sqrt(two_features_mse)

## 9. Using more features ##

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

knn.fit(train_df[['accommodates','bedrooms','bathrooms','number_of_reviews']],train_df['price'])

four_predictions=knn.predict(test_df[['accommodates','bedrooms','bathrooms','number_of_reviews']])
four_mse=mean_squared_error(four_predictions,test_df['price'])

import math
four_rmse=math.sqrt(four_mse)

## 10. Using all features ##

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

knn.fit(train_df.drop(columns='price'),train_df['price'])

all_features_predictions=knn.predict(test_df.drop(columns='price'))
all_features_mse=mean_squared_error(all_features_predictions,test_df['price'])

import math
all_features_rmse=math.sqrt(all_features_mse)