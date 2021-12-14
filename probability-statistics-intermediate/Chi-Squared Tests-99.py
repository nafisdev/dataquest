## 2. Calculating Differences ##

female_diff=(10771-16280.5)/16280.5
male_diff=(21790-16280.5)/16280.5

## 3. Updating the Formula ##

female_diff=(10771-16280.5)**2/16280.5
male_diff=(21790-16280.5)**2/16280.5
gender_chisq=female_diff+male_diff

## 4. Generating a Distribution ##

chi_squared_values = []
import numpy as np

for i in range(1000):
    li=list(np.random.random_sample(32561,))
    # print(len(li))
    l=[]
    # print(len(l))
    for a in li:
        if a < 0.5:
            l.append(0)
        else:
            l.append(1)
            
    om=l.count(0)
    of=l.count(1)
    male_diff=(om-16280.5)**2/16280.5
    female_diff=(of-16280.5)**2/16280.5
    chi_squared_values.append(male_diff+female_diff)
# print(chi_squared_values)
import matplotlib.pyplot as plt

plt.hist(chi_squared_values)

## 6. Smaller Samples ##

female_diff=(162.805-107.71)**2/162.805

male_diff=(162.805-217.90)**2/162.805


gender_chisq=male_diff+female_diff

## 7. Sampling Distribution Equality ##

chi_squared_values = []
for i in range(1000):
    li=list(np.random.random_sample(300,))
    # print(len(li))
    l=[]
    # print(len(l))
    for a in li:
        if a < 0.5:
            l.append(0)
        else:
            l.append(1)
            
    om=l.count(0)
    of=l.count(1)
    male_diff=(om-150)**2/150
    female_diff=(of-150)**2/150
    chi_squared_values.append(male_diff+female_diff)
# print(chi_squared_values)
import matplotlib.pyplot as plt

plt.hist(chi_squared_values)

## 9. Increasing Degrees of Freedom ##

race_chisq=((26146.5-27816)**2/26146.5 +(3124-3939.9)**2/3939.9 +(944.3-1039)**2/944.3 +(260.5-311)**2/260.5 +(271-1269.8)**2/1269.8)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

a, race_pvalue=chisquare([27816,3124,1039,311,271],[26146.5,3939.9,944.3,260.5,1269.8])