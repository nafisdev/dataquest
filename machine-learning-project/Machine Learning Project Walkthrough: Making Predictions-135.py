## 1. Recap ##

import pandas as pd

loans=pd.read_csv('clean_loans_2007.csv')

print(loans.info())

## 3. Picking an Error Metric ##

import pandas as pd

tn=(predictions==0) & (loans['loan_status']==0)
tn=len(predictions[tn])
tp=(predictions==1) & (loans['loan_status']==1)
tp=len(predictions[tp])
fn=(predictions==0) & (loans['loan_status']==1)
fn=len(predictions[fn])
fp=(predictions==1) & (loans['loan_status']==0)
fp=len(predictions[fp])

## 5. Class Imbalance ##

import pandas as pd
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))

tn=(predictions==0) & (loans['loan_status']==0)
tn=len(predictions[tn])
tp=(predictions==1) & (loans['loan_status']==1)
tp=len(predictions[tp])
fn=(predictions==0) & (loans['loan_status']==1)
fn=len(predictions[fn])
fp=(predictions==1) & (loans['loan_status']==0)
fp=len(predictions[fp])

fpr=fp/(fp+tn)
tpr=tp/(tp+fn)

## 6. Logistic Regression ##

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

features=loans.drop(columns='loan_status')
target=loans['loan_status']

lr.fit(features,target)

predictions=lr.predict(features)

## 7. Cross Validation ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
lr = LogisticRegression()

predictions=pd.Series(cross_val_predict(lr,features,target, cv=3))

tn=(predictions==0) & (loans['loan_status']==0)
tn=len(predictions[tn])
tp=(predictions==1) & (loans['loan_status']==1)
tp=len(predictions[tp])
fn=(predictions==0) & (loans['loan_status']==1)
fn=len(predictions[fn])
fp=(predictions==1) & (loans['loan_status']==0)
fp=len(predictions[fp])

fpr=fp/(fp+tn)
tpr=tp/(tp+fn)

## 9. Penalizing the Classifier ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

lr=LogisticRegression(class_weight='balanced')

predictions=pd.Series(cross_val_predict(lr,features,target, cv=3))

tn=(predictions==0) & (loans['loan_status']==0)
tn=len(predictions[tn])
tp=(predictions==1) & (loans['loan_status']==1)
tp=len(predictions[tp])
fn=(predictions==0) & (loans['loan_status']==1)
fn=len(predictions[fn])
fp=(predictions==1) & (loans['loan_status']==0)
fp=len(predictions[fp])

fpr=fp/(fp+tn)
tpr=tp/(tp+fn)

## 10. Manual Penalties ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
penalty = {
    0: 10,
    1: 1
}
lr=LogisticRegression(class_weight=penalty)

predictions=pd.Series(cross_val_predict(lr,features,target, cv=3))

tn=(predictions==0) & (loans['loan_status']==0)
tn=len(predictions[tn])
tp=(predictions==1) & (loans['loan_status']==1)
tp=len(predictions[tp])
fn=(predictions==0) & (loans['loan_status']==1)
fn=len(predictions[fn])
fp=(predictions==1) & (loans['loan_status']==0)
fp=len(predictions[fp])

fpr=fp/(fp+tn)
tpr=tp/(tp+fn)

## 11. Random Forests ##

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict

lr=RandomForestClassifier(random_state=1,class_weight='balanced')

predictions=pd.Series(cross_val_predict(lr,features,target, cv=3))

tn=(predictions==0) & (loans['loan_status']==0)
tn=len(predictions[tn])
tp=(predictions==1) & (loans['loan_status']==1)
tp=len(predictions[tp])
fn=(predictions==0) & (loans['loan_status']==1)
fn=len(predictions[fn])
fp=(predictions==1) & (loans['loan_status']==0)
fp=len(predictions[fp])

fpr=fp/(fp+tn)
tpr=tp/(tp+fn)