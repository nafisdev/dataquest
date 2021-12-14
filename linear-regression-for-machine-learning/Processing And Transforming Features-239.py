## 1. Introduction ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()
print(train_null_counts[train_null_counts==0].index)

df_no_mv=train[train_null_counts[train_null_counts==0].index]

## 2. Categorical Features ##

text_cols = df_no_mv.select_dtypes(include=['object']).columns

for col in text_cols:
    # print(col+":", len(train[col].unique()))
    train[col]=train[col].astype('category')
    # train[col]=train[col].cat.codes
    
# train['Utilities']= train['Utilities'].cat.codes
print(train['Utilities'].cat.codes.value_counts())

## 3. Dummy Coding ##

dummy_cols = pd.DataFrame()
print(pd.get_dummies(train['Utilities'])) 
for col in text_cols:
    col_dummies = pd.get_dummies(train[col])
    train = pd.concat([train, col_dummies], axis=1)
    del train[col]

## 4. Transforming Improper Numerical Features ##

train['years_until_remod']=train['Year Remod/Add']-train['Year Built']

## 5. Missing Values ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()

df_missing_values=train[train.columns[(train_null_counts>0) & (train_null_counts <584)]]
# df_missing_values.info()

## 6. Imputing Missing Values ##

float_cols = df_missing_values.select_dtypes(include=['float'])

float_cols=float_cols.fillna(float_cols.mean())
float_cols.isnull().sum()