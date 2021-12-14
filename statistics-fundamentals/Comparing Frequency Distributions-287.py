## 2. Grouped Bar Plots ##

import seaborn as sns

sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba, order=['Rookie', 'Little experience', 'Experienced','Very experienced','Veteran'], hue_order=['C', 'F','F/C','G' ,'G/F'])



## 3. Challenge: Do Older Players Play Less? ##

wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else
                                           'below average')

import seaborn as sns

sns.countplot(x = 'age_mean_relative', hue = 'min_mean_relative', data = wnba)

result='rejection'

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt

wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)

plt.axvline(label='Average', x=497)
plt.legend()
plt.show()

## 5. Kernel Density Estimate Plots ##

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
import matplotlib.pyplot as plt
plt.axvline(label='Average', x=497)
plt.legend()
plt.show()

## 7. Strip Plots ##

sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)
plt.show()

## 8. Box plots ##

sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)
plt.show()

## 9. Outliers ##

iqr=7
lower_bound=11.5
upper_bound=39.5

sns.boxplot(wnba['Games Played'])

outliers_high=0
outliers_low=wnba[wnba['Games Played']<11.5].shape[0]
plt.show()