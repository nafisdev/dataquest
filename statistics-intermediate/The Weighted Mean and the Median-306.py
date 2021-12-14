## 1. Introduction ##

mean_new=houses_per_year['Mean Price'].mean()

mean_original=houses['SalePrice'].mean()

difference=mean_original-mean_new

## 2. Different Weights ##

weighted_mean=(houses_per_year['Mean Price']*houses_per_year['Houses Sold']).sum()/houses_per_year['Houses Sold'].sum()

mean_original=houses['SalePrice'].mean()

difference=mean_original-weighted_mean

## 3. The Weighted Mean ##

import numpy as np

def wfunc(arr1,arr2):
    w=0
    arr1=list(arr1)
    arr2=list(arr2)
    for a in range(len(arr1)):
        w+=arr1[a]*arr2[a]
    weighted_mean=w/sum(arr2)
    return weighted_mean


arr1=houses_per_year['Mean Price']
arr2=houses_per_year['Houses Sold']
weighted_mean_function=wfunc(arr1,arr2)
    
    
weighted_mean_numpy = np.average(arr1, weights=arr2)

equal=weighted_mean_numpy==weighted_mean_function

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']


median1=23
median2=55
median3=32

## 5. Distributions with Even Number of Values ##

median=(houses['TotRms AbvGrd'].replace('10 or more',10).astype(int).sort_values()[1465])

## 6. The Median as a Resistant Statistic ##

# houses['Lot Area'].plot.box()
# houses['SalePrice'].plot.box()

lotarea_difference=houses['Lot Area'].mean()-houses['Lot Area'].median()
saleprice_difference=houses['SalePrice'].mean()-houses['SalePrice'].median()

## 7. The Median for Ordinal Scales ##

mean=houses['Overall Cond'].mean()
median=houses['Overall Cond'].median()


houses['Overall Cond'].plot.hist()
more_representative='mean'