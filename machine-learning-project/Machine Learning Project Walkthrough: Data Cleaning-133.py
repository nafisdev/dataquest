## 3. Reading into Pandas ##

import pandas as pd

loans_2007=pd.read_csv('loans_2007.csv')

print(loans_2007.iloc[0,:])
print(loans_2007.shape[1])

## 5. First Group of Columns ##

loans_2007=loans_2007.drop(columns=['id','member_id','funded_amnt','funded_amnt_inv','grade','sub_grade','emp_title','issue_d'])

## 7. Second Group of Features ##

loans_2007=loans_2007.drop(columns=['zip_code','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_pymnt_inv','total_rec_prncp'])

## 9. Third Group of Features ##

loans_2007=loans_2007.drop(columns=['total_rec_int','total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_d','last_pymnt_amnt'])

## 10. Target Column ##

print(loans_2007['loan_status'].value_counts())

## 12. Binary Classification ##

loans_2007=loans_2007[loans_2007['loan_status'].apply(lambda x: x in ['Fully Paid','Charged Off'])]

loans_2007=loans_2007.replace('Fully Paid',1)

loans_2007=loans_2007.replace('Charged Off',0)
# a='as' not in ['aa']

## 13. Removing Single Value Columns ##

drop_columns=[]
for i in loans_2007.columns:
    a=loans_2007[i].value_counts()
    # print(a)
    # print(len(a))
    if(len(a)==1):
        # 
        drop_columns.append(a.name)
        
loans_2007=loans_2007.drop(columns=drop_columns)