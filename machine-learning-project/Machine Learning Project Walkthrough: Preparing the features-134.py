## 1. Recap ##

import pandas as pd

loans=pd.read_csv('filtered_loans_2007.csv')
# null_counts=

null_counts = loans.isnull().sum()

## 2. Handling Missing Values ##

print(loans.pub_rec_bankruptcies.value_counts(normalize=True, dropna=False))


loans=loans.drop(columns=['pub_rec_bankruptcies'])

loans=loans.dropna()
print(loans.dtypes.value_counts())

## 3. Text Columns ##

object_columns_df = loans.select_dtypes(include=['object'])

print(object_columns_df.iloc[0,:])

## 5. First 5 Categorical Columns ##

cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']


for i in cols:
    print(loans[i].value_counts())

## 6. The Reason for The Loan ##

print(loans['title'].value_counts())
print(loans['purpose'].value_counts())

## 7. Categorical Columns ##

mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}

loans=loans.drop(columns=['last_credit_pull_d', 'addr_state', 'title', 'earliest_cr_line'])

loans['int_rate']=loans['int_rate'].str.rstrip('%').astype('float')
loans['revol_util']=loans['revol_util'].str.rstrip('%').astype('float')

loans['emp_length']=loans['emp_length'].replace(mapping_dict['emp_length'])

## 8. Dummy Variables ##

cat_columns = ["home_ownership", "verification_status", "purpose", "term"]
dummy_df = pd.get_dummies(loans[cat_columns])
loans = pd.concat([loans, dummy_df], axis=1)
loans = loans.drop(cat_columns, axis=1)