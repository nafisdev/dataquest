## 2. Introduction to the data ##

import pandas as pd

dc_listings=pd.read_csv('dc_airbnb.csv')
print(dc_listings)




## 4. Euclidean Distance ##

import numpy as np
# print(dc_listings)

import math
# print()
first_distance =math.sqrt((3-int(dc_listings.loc[0,['accommodates']]))**2)

print(first_distance)


## 5. Calculate Distance for All Observations ##

import math

dc_listings['distance'] =dc_listings['accommodates'].apply(lambda x: int(math.sqrt((3-x)**2)))

print(dc_listings['distance'].value_counts())

## 6. Randomizing and Sorting ##

import numpy as np
np.random.seed(1)

dc_listings=dc_listings.loc[np.random.permutation(3723),:]
dc_listings=dc_listings.sort_values(by='distance')

print(dc_listings.head(10))

## 7. Average price ##

# def clean(elem):
    

dc_listings['price']=dc_listings['price'].str.replace('$','').str.replace(',', '')


dc_listings['price']=dc_listings['price'].astype(float)

mean_price=dc_listings['price'].head(5).mean()
print(mean_price)

## 8. Function to Make Predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
import math
def predict_price(new_listing):
    temp_df = dc_listings.copy()
    temp_df['distance'] =temp_df['accommodates'].apply(lambda x: int(math.sqrt((new_listing-x)**2)))
    temp_df=temp_df.sort_values(by='distance')
    predict_price=temp_df['price'].head(5).mean()
    return predict_price
    ## Complete the function.
    
    
    # return(new_listing)

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)