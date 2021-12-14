## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]
sum(distribution)

mean=4
center=False
equal_distances=True

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed

equal_distances=0
for a in range(5000):
    seed(seed=a)
    arr=randint(1000,size=10)
    # print(arr)
    mean=round(arr.mean(),1)
    # print(mean)
    if round(sum(arr-mean),1)==0:
        equal_distances+=1

## 4. Defining the Mean Algebraically ##

one=False

two=False
three=False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]
mean_1=sum(distribution_1)/4
mean_2=sum(distribution_2)/7
mean_3=sum(distribution_3)/7

## 6. Introducing the Data ##

houses=pd.read_table('AmesHousing_1.txt',sep = '\t')
print(houses.head())
one=True
two=False
three=True

## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean=mean(houses['SalePrice'])
pandas_mean=houses['SalePrice'].mean()
means_are_equal=function_mean==pandas_mean

## 8. Estimating the Population Mean ##

# print(houses['Yr Sold'].min())
# b=(houses['Yr Sold']>=2006) & (houses['Yr Sold']<=2010)
houses=houses[b]
c=5
sampling_errors=[]
sample_sizes=[]
parameter=houses['SalePrice'].mean()
for i in range(0,101,1):
    statistic=houses['SalePrice'].sample(random_state=i,n=c).mean()
    sampling_errors.append(parameter-statistic)
    sample_sizes.append(c)
    c+=29
    
    
plt.scatter(sample_sizes,sampling_errors)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')
plt.axhline(y=0)
plt.axvline(x=2930)
plt.show()

## 9. Estimates from Low-Sized Samples ##

means = []
for i in range(10000):
    sample = houses['SalePrice'].sample(n=100, random_state=i)
    means.append(sample.mean())

plt.hist(means)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim((0,500000))
# 58195.859999999986

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]

unbiased=mean([5,2.5,4.5])==mean(population)