## 2. Calculating Expected Values ##

males_over50k=32561*0.241*0.67

males_under50k=32561*0.759*0.67

females_over50k=32561*0.241*0.33

females_under50k=32561*0.759*0.33

## 3. Calculating Chi-squared ##

chisq_gender_income= (5257.6-6662)**2/5257.6 + (16558.2-15128)**2/16558.2 + (2589.6-1179)**2/2589.6 + (8155.6-9592)**2/8155.6

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare
observed=[6662,1179,15128,9592]
expected=[5257.6,2589.6,16558.2,8155.6]
k, pvalue_gender_income=chisquare(observed, expected)

## 5. Cross Tables ##

import pandas

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding Expected Values ##

import numpy as np
from scipy.stats import chi2_contingency
observed = pandas.crosstab(income["sex"], [income["race"]])#np.array([[5, 5], [10, 10]])

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(observed)