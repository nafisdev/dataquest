## 1. Reading CSV files with NumPy ##

import numpy as np

taxi=np.genfromtxt("nyc_taxis.csv", delimiter=',')
taxi_shape=taxi.shape

## 2. Reading CSV Files with NumPy Continued ##

import numpy as np
taxi = np.genfromtxt("nyc_taxis.csv", delimiter=',', skip_header=1)
taxi_shape=taxi.shape
import csv 
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# # remove the header row
# taxi_list = taxi_list[1:]

# # convert all values to floats
# converted_taxi_list = []
# for row in taxi_list:
#     converted_row = []
#     for item in row:
#         converted_row.append(float(item))
#     converted_taxi_list.append(converted_row)

# # start writing your code below this comment
# taxi = np.array(converted_taxi_list)

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])


a_bool=a<3
b_bool=b=="blue"
c_bool=c>100

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool =pickup_month == 2
february=pickup_month[february_bool]
february_rides=february.shape[0]

## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]

tip_bool=tip_amount>50

top_tips=taxi[tip_bool,5:14]

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
taxi_modified[1066][5]=1

taxi_modified[:,0]=taxi_modified[:,0]%100

print(taxi_modified[550:552,7])
taxi_modified[550:552,7]=np.mean(taxi_modified[550:552,7])

## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()

total_amount=taxi_copy[:,13]
taxi_copy[total_amount<0]=0

## 8. Assignment Using Boolean Arrays Continued ##

# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)


taxi_modified[taxi_modified[:,5]==2,15]=1
taxi_modified[taxi_modified[:,5]==3,15]=1
taxi_modified[taxi_modified[:,5]==5,15]=1

## 9. Challenge: Which Is the Most Popular Airport? ##

a=np.sum(taxi[:,6]==2)
jfk_count=int(np.sum(taxi[:,6]==2))
laguardia_count=int(np.sum(taxi[:,6]==3))
newark_count=int(np.sum(taxi[:,6]==5))

## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
cleaned_taxi=taxi[trip_mph<100,:]


mean_distance=np.mean(cleaned_taxi[:,7])
mean_length=np.mean(cleaned_taxi[:,8])
mean_total_amount=np.mean(cleaned_taxi[:,13])