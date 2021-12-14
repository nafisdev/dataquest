## 1. Introduction ##

houses=pd.read_table('AmesHousing_1.txt')
print(houses.head())

scale_land='ordinal'

scale_roof='nominal'

kitchen_variable='discrete'

## 2. The Mode for Ordinal Variables ##

def modedic(arr):
    arr=list(arr)
    dic={}
    maxa=0
    out=0
    for a in arr:
        if a in dic:
            dic[a]+=1
            if(maxa<dic[a]):
                maxa=dic[a]
                out=a
        else:
            dic[a]=1
    print(max(dic, key=dic.get))
    return out


mode_function=modedic(houses['Land Slope'])

mode_method=houses['Land Slope'].mode()
same=mode_function==mode_method



     

## 3. The Mode for Nominal Variables ##

# The function we wrote (you can copy-paste yours from the previous screen)
def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return max(counts, key = counts.get), counts



mode, value_counts=mode(houses['Roof Style'])

vc=houses['Roof Style'].value_counts()

## 4. The Mode for Discrete Variables ##

houses.head(10)

bedroom_variable='discrete'

bedroom_mode=houses['Bedroom AbvGr'].mode()

price_variable='continuous'

price_mode=houses['SalePrice'].mode()

## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)

mode=150000

mean=houses['SalePrice'].mean()
median=houses['SalePrice'].median()

sentence_1=True

sentence_2=True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}


shape_1='right skew'

shape_2='right skew'

shape_3='left skew'

## 7. Symmetrical Distributions ##

houses['Mo Sold'].plot.kde(xlim=(1,12))
import matplotlib.pyplot as plt
print(houses['Mo Sold'].median())
plt.axvline(int(houses['Mo Sold'].mode()), color = 'Green',label = 'Mode')
plt.axvline(houses['Mo Sold'].median(), color = 'Orange',label = 'Median')
plt.axvline(houses['Mo Sold'].mean(), color = 'Black',label = 'Mean')
plt.legend()


# import matplotlib.pyplot as plt
# plt.axvline(150000, color = 'Green')