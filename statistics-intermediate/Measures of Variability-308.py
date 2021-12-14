## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def retran(arr):
    return max(arr)-min(arr)
range_by_year ={}
for a in range(2006,2011):#retran(houses['Yr Sold']):
    hy=houses[houses['Yr Sold']==a]
    range_by_year[a]=retran(hy['SalePrice'])

    
    
one = False
two = True

## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

m=sum(C)/len(C)
def avgdist(arr):
    s=0
    for a in arr:
        s+=(m-a)
    return s/len(arr)

avg_distance=avgdist(C)

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

m=sum(C)/len(C)
def avgdist(arr):
    s=0
    for a in arr:
        s+=abs(m-a)
    return s/len(arr)


mad=avgdist(C)

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

m=sum(C)/len(C)
def avgdist(arr):
    s=0
    for a in arr:
        s+=pow(m-a,2)
    return s/len(arr)

variance_C=avgdist(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

m=sum(C)/len(C)
def avgdist(arr):
    s=0
    for a in arr:
        s+=pow(m-a,2)
    return s/len(arr)

standard_deviation_C=sqrt(avgdist(C))

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)
# std=standard_deviation(houses['Yr Sold'])
range_by_year={}
for a in range(2006,2011):#retran(houses['Yr Sold']):
    hy=houses[houses['Yr Sold']==a]
    range_by_year[a]=standard_deviation(hy['SalePrice'])
    
lowest_variability=2010
greatest_variability=2006

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)


bigger_spread='sample 2'

st_dev1=standard_deviation(sample1)

st_dev2=standard_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

std=[]
for i in range(5000):
    sample=houses['SalePrice'].sample(n=10, random_state=i)
    std.append(standard_deviation(sample))

plt.hist(std)
plt.axvline(standard_deviation(houses['SalePrice']))

## 9. Bessel's Correction ##

from math import sqrt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    l=len(distances)-1
    
    variance = sum(distances) / l
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

plt.hist(st_devs)
plt.axvline(pop_stdev)  # pop_stdev is pre-saved from the last screen

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var


pandas_stdev=sample['SalePrice'].std(ddof=1)

numpy_stdev=std(sample['SalePrice'],ddof=1)

equal_stdevs=pandas_stdev==numpy_stdev

pandas_var=sample['SalePrice'].var()

numpy_var=var(sample['SalePrice'],ddof=1)

equal_vars=pandas_var==numpy_var

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

equal_var=False

equal_stdev=False