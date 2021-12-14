## 2. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt

admissions=pd.read_csv('admissions.csv')

admissions.plot(x='gpa',y='admit', kind='scatter')
# plt.xlabel('gpa')
# plt.ylabel('admit')
plt.xlabel('')
plt.ylabel('')


plt.show()

## 5. Training a Logistic Regression Model ##

from sklearn.linear_model import LinearRegression
linear_model = LinearRegression()
linear_model.fit(admissions[["gpa"]], admissions["admit"])


from sklearn.linear_model import LogisticRegression 
logistic_model =LogisticRegression ()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])

## 6. Plotting Probabilities ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])


pred_probs=logistic_model.predict_proba(admissions[['gpa']])

from matplotlib import pyplot as plt

plt.scatter(x=admissions['gpa'],y=pred_probs[:,1])

## 7. Predict Labels ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])

fitted_labels=logistic_model.predict(admissions[['gpa']])

from matplotlib import pyplot as plt

plt.scatter(x=admissions['gpa'],y=fitted_labels)