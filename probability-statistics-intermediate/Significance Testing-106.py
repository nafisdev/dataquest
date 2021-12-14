## 3. Statistical Significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)
mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

## 4. Test Statistic ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)
mean_difference=mean_group_b-mean_group_a
print(mean_difference)

## 5. Permutation Test ##

mean_difference = 2.52
print(all_values)
mean_differences=[]

import numpy as np
for i in range(1000):
    group_a=[]
    group_b=[]
    for a in all_values:
        r=np.random.rand()
        if r>=0.5:
            group_a.append(a)
        else:
            group_b.append(a)
    iteration_mean_difference=np.mean(group_b)-np.mean(group_a)
    mean_differences.append(iteration_mean_difference)
from matplotlib import pyplot as plt    
plt.hist(mean_differences)
    
        

## 7. Dictionary Representation of a Distribution ##

w="Help"
w.lower()
print(w)
sampling_distribution={}
for i in mean_differences:
    if sampling_distribution.get(i,False):
        sampling_distribution[i]+=1
    else:
        sampling_distribution[i]=1
        
    

## 8. P Value ##

frequencies =[]


for i in sampling_distribution:
    if i > 2.52:
        frequencies.append(i)

p_value=np.sum(frequencies)/1000