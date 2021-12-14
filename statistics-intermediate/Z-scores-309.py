## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

houses['SalePrice'].plot.kde(xlim=(houses['SalePrice'].min(),houses['SalePrice'].max()))

plt.axvline(houses['SalePrice'].mean(), color='black', label='Mean')


plt.axvline(houses['SalePrice'].mean()+houses['SalePrice'].std(ddof=0), color='red',label='Standard deviation')

plt.axvline(220000, color='orange', label='220000')

plt.legend()




very_expensive=False

## 2. Number of Standard Deviations ##

print(houses['SalePrice'].mean())
print(houses['SalePrice'].std())

st_devs_away=(220000-houses['SalePrice'].mean())/houses['SalePrice'].std(ddof=0)

## 3. Z-scores ##

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

import numpy as np
s=np.std(houses['SalePrice'],ddof=0)
min_z=(min_val-mean_val)/s
mean_z=(mean_val-mean_val)/s
max_z=(max_val-mean_val)/s

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z
# print(list(houses[houses['Neighborhood'] == 'NAmes']['SalePrice']))
print(z_score(200000,list(houses[houses['Neighborhood'] == 'NAmes']['SalePrice'])))
print(z_score(200000,houses[houses['Neighborhood'] == 'CollgCr']['SalePrice']))
print(z_score(200000,houses[houses['Neighborhood'] == 'OldTown']['SalePrice']))
print(z_score(200000,houses[houses['Neighborhood'] == 'Edwards']['SalePrice']))
print(z_score(200000,houses[houses['Neighborhood'] == 'Somerst']['SalePrice']))

best_investment='College Creek'

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )


z_mean_price=houses['z_prices'].mean()

z_stdev_price=houses['z_prices'].std(ddof=0)


LA = houses['Lot Area'].apply(
    lambda x: ((x - houses['Lot Area'].mean()) / houses['Lot Area'].std(ddof = 0))
    )

z_mean_area=LA.mean()

z_stdev_area=LA.std(ddof=0)

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]

population=[((x - mean(population)) / std(population)) for x in population]
mean_z=mean(population)
stdev_z=std(population)

## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 0)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample=std(standardized_sample)

## 8. Using Standardization for Comparisons ##

index_1 = houses['index_1'].apply(
    lambda x: ((x - houses['index_1'].mean()) / houses['index_1'].std())
    )

index_2 = houses['index_2'].apply(
    lambda x: ((x - houses['index_2'].mean()) / houses['index_2'].std())
    )

print(index_1[0:2])
print(index_2[0:2])

better='first'

## 9. Converting Back from Z-scores ##

import numpy as np

mean_transformed=np.mean([a*10+50 for a in houses['z_merged']])
stdev_transformed=np.std([a*10+50 for a in houses['z_merged']],ddof=0)