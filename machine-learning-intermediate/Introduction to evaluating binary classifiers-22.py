## 1. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")
model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])

labels=model.predict(admissions[["gpa"]])

admissions['predicted_label']=labels

print(admissions['predicted_label'])

print(admissions.head())

## 2. Accuracy ##

admissions=admissions.rename(columns={'admit':'actual_label'})
matches=admissions['actual_label']==admissions['predicted_label']

correct_predictions=admissions[matches]


print(correct_predictions.head())

accuracy=matches.sum()/len(matches)
print(accuracy)

## 4. Binary classification outcomes ##

true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])

print(true_positives)
print(true_negatives)

## 5. Sensitivity ##

# From the previous screen
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])

sensitivity=true_positives/(true_positives+false_negatives)

## 6. Specificity ##

# From previous screens
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])
true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])

false_positives_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 0)

false_positives = len(admissions[false_positives_filter])

specificity=true_negatives/(false_positives+true_negatives)