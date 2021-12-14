## 2. Communication is a Two-way Street ##

# ans = "A"
# ans = "B"
ans = "C"

## 3. Dealing with Fuzzy Language ##

ans = "A"
# ans = "B"
# ans = "C"

## 4. Churned Customers ##

import pandas as pd
from datetime import datetime as dt

data = pd.read_csv("rfm_xmas19.txt", parse_dates=["trans_date"])
group_by_customer = data.groupby("customer_id")
last_transaction = group_by_customer["trans_date"].max()

best_churn=pd.DataFrame(last_transaction)

cutoff_day = dt.strptime('Oct 16 2019', '%b %d %Y')
best_churn["churned"]=best_churn["trans_date"].apply(lambda x: int(x<cutoff_day))
print(len(last_transaction))

## 5. Aggregate Data by Customer ##

best_churn["nr_of_transactions"] = group_by_customer.size()
best_churn['amount_spent']=group_by_customer['tran_amount'].sum()
best_churn=best_churn.drop(columns=['trans_date'])

## 6. Ranking Customers ##

import pandas as pd
import datetime as dt

data = pd.read_csv("rfm_xmas19.txt", parse_dates=["trans_date"])
group_by_customer = data.groupby("customer_id")
last_transaction = group_by_customer["trans_date"].max()

best_churn = pd.DataFrame(last_transaction)

cutoff_day = dt.datetime(2019, 10, 16)

best_churn["churned"] = best_churn["trans_date"].apply(
    lambda date: 1 if date < cutoff_day else 0
)

best_churn["nr_of_transactions"] = group_by_customer.size()
best_churn["amount_spent"] = group_by_customer.sum()
best_churn.drop("trans_date", axis="columns", inplace=True)
minnr=best_churn[['nr_of_transactions']].min()
maxnr=best_churn[['nr_of_transactions']].max()
minam=best_churn[['amount_spent']].min()
maxam=best_churn[['amount_spent']].max()
best_churn[['scaled_tran']]=(best_churn[['nr_of_transactions']]-minnr)/(maxnr-minnr)

best_churn[['scaled_amount']]=(best_churn[['amount_spent']]-minam)/(maxam-minam)

best_churn['score']=best_churn['scaled_amount']+best_churn['scaled_tran']


best_churn['score']=best_churn['score']*50


best_churn.sort_values(by='score',ascending=False,inplace=True)

## 7. Determining a Threshold ##

print(data.describe())
coupon=float(data[['tran_amount']].mean()*0.3)

nr_of_customers=1000/coupon

## 8. Delivering the Results ##

print(coupon, nr_of_customers, sep="\n")

top_50_churned=best_churn[best_churn['churned']==1].iloc[0:50,:]

top_50_churned.to_csv('best_customers.txt')