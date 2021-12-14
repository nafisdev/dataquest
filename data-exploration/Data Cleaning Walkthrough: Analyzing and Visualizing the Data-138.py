## 3. Finding Correlations With the r Value ##

correlations=combined.corr()['sat_score']

## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt


combined.plot.scatter(x="total_enrollment", y="sat_score")
plt.show()

## 6. Exploring Schools with Low SAT Scores and Enrollment ##

low_enrollment=combined[combined['total_enrollment']<1000]
low_enrollment=combined[combined['sat_score']<1000]


print(low_enrollment['School Name'])

## 7. Plotting Language Learning Percentage ##

import matplotlib.pyplot as plt


combined.plot.scatter(x="ell_percent", y="sat_score")
plt.show()

## 8. Calculating District-Level Statistics ##

import numpy as np


districts=combined.groupby('school_dist').agg(np.mean)
districts.reset_index(inplace=True)



print(districts.head())