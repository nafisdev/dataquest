## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings=dc_listings.loc[np.random.permutation(dc_listings.shape[0]),:]
split_one=dc_listings[:1862]
split_two=dc_listings[1862:]

## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import math
train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one



knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
knn.fit(train_one[['accommodates']], train_one[['price']])
predictions = knn.predict(test_one[['accommodates']])
iteration_one_rmse =math.sqrt(mean_squared_error(test_one['price'], predictions))

knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
knn.fit(train_two[['accommodates']], train_two[['price']])
predictions = knn.predict(test_two[['accommodates']])
iteration_two_rmse = math.sqrt(mean_squared_error(test_two[['price']], predictions))

avg_rmse=np.mean([iteration_one_rmse,iteration_two_rmse])

## 3. K-Fold Cross Validation ##

dc_listings['fold']=dc_listings.index

def ran(el):
    if el<745:
        return 1
    if el<1490:
        return 2
    if el<2234:
        return 3
    if el<2978:
        return 4
    else:
        return 5
    # return int((el)/745)+1
dc_listings['fold']=dc_listings['fold'].apply(ran)
dc_listings['fold']=dc_listings['fold'].astype(float)

dc_listings['fold'].value_counts()

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
# mask=(dc_listings['fold']==1)
# print(mask)
knn.fit(dc_listings[dc_listings['fold']!=1].loc[:,['accommodates']], dc_listings[dc_listings['fold']!=1].loc[:,['price']])
labels = knn.predict(dc_listings[dc_listings['fold']==1][['accommodates']])
iteration_one_rmse =math.sqrt(mean_squared_error(dc_listings[dc_listings['fold']==1]['price'], labels))

## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
import math
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

fold_ids = [1,2,3,4,5]
rmses=[]
def train_and_validate(df,fold_ids):
    for a in fold_ids:
        knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
        # mask=(dc_listings['fold']==1)
        # print(mask)
        knn.fit(dc_listings[dc_listings['fold']!=a].loc[:,['accommodates']], dc_listings[dc_listings['fold']!=a].loc[:,['price']])
        labels = knn.predict(dc_listings[dc_listings['fold']==a][['accommodates']])
        rmses.append(math.sqrt(mean_squared_error(dc_listings[dc_listings['fold']==a]['price'], labels)))
        
train_and_validate(dc_listings,fold_ids)     
avg_rmse=np.mean(rmses)
print(rmses)
print(avg_rmse)

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold

kf = KFold(5, shuffle=True ,random_state=1)
knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
mses=cross_val_score(knn, dc_listings[["accommodates"]], dc_listings[["price"]], scoring="neg_mean_squared_error", cv=kf)

import numpy as np
import math
# a=math.sqrt(4)
rmses=[math.sqrt(abs(a)) for a in mses]
avg_rmse=np.mean(rmses)